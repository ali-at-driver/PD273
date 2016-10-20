from config import Adapters
from contextlib import contextmanager
from cStringIO import StringIO
from cutadapt.scripts import cutadapt

import re
import os 
import subprocess
import sys
import tempfile # FIXME: immutable

"""TODO
general
  Improve regex searches, report output 
  TRY/Excepts
  param overrides

get_adapter()
    #TODO: find a way to retrieve using cutadapt, forexample
run()
    # TODO improve redirect of standard output
    # TODO diff log files
    # TODO: implement param override

grep_report():
   # TODO: more sophisticated regex....
   # TODO: MAKE THIS FUNCTION BETTER
"""


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout


@contextmanager
def temporary_path(name):
    #    directory = os.path.join(os.path.dirname(__file__))
    #    if not os.path.isdir(directory):
    #        os.mkdir(directory)
    path = os.path.join(name)
    yield path
    os.remove(path)


def datapath(path):
    return os.path.join(os.path.dirname(__file__), path)


def get_adapter(infile, pre_adapter, read_num):
    try: 
        p1 = subprocess.Popen(["zcat", infile], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["head", "-n", "1"], stdin=p1.stdout, stdout=subprocess.PIPE)
        output = p2.communicate()[0]
    except AttributeError:
        print("ABORTING READ; FILE ERROR; FIXME")

    # inserts is the read specific sequence that replaces the X*8 repeats in the lab adapter
    # more specific var name TBD
    inserts = re.search(Adapters.insert_re, output) # TODO: more stringent regex
    
    if inserts:  # TODO: one or both? O|1
        p1.kill()
        p2.stdout.close()
        return pre_adapter.replace(Adapters.replace, inserts.group(read_num))  # TODO: FIXME

    return None


def run(infile, outfile="/dev/null", params=None, lab_adapt_override=None, stdout_override=True):
    if type(params) is str:
        params = params.split()

    # DO CHECKS
    read_num = 0 if re.search('R1', infile) else 1

    if lab_adapt_override is None:  # pythonic?
        pre_adapter = Adapters.lab0 if read_num == 0 else Adapters.lab1
    
    # cutadapt can get cranky if these are too long
    params = ['-a', get_adapter(infile, pre_adapter, read_num),
              '-o', outfile, datapath(infile)]
    # TODO parallelizable?
    # TODO: add infile2
    if stdout_override:
        with Capturing() as output:
            cutadapt.main(params)
            return output
    else:
        return cutadapt.main(params)

def run_paired(infile0, infile1, tmpfile=None, tmpfile1=None, params=None, stdout=True):
    # TODO: implement params AND param override 
    if type(params) is str:
        params = params.split()

    output0 = run(infile0, stdout_override=stdout)
    output1 = run(infile1, stdout_override=stdout)
    #print(output0)
    #print(output1)
    #print("\n\n")
    
    return (output0, output1)

    
