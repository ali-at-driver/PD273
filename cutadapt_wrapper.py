from contextlib import contextmanager
import tempfile # FIXME: immutable
import subprocess
from cutadapt.scripts import cutadapt

import re
import os

from cStringIO import StringIO
import sys

"""
residuals -- please ignore -- pre-git setup on cluster :)
class Constants:
    read0 = 0
    read1 = 1

p3 = subprocess.Popen(["cutadapt", "-a", adapters.adp, "-o", ""])#, stdin=p1.stdout, stdout=subprocess.PIPE)

TODO: get opinion on static vars vs import 'config' file

Will other modules in this project benefit from having a config file to read from later?

"""

class Adapters:
    lab0 = "AATGATACGGCGACCACCGAGATCTACACXXXXXXXXACACTCTTTCCCTACACGACGCTCTTCCGATCT"
    lab1= "GATCGGAAGAGCACACGTCTGAACTCCAGTCACXXXXXXXXATCTCGTATGCCGTCTTCTGCTTG"

# FIXME
REPORT_FIELD='Reads with adapters:'

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
    """ TODO: find a way to retrieve using cutadapt, forexample
    """
    print(infile)
    try:
        p1 = subprocess.Popen(["zcat", infile], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["head", "-n", "1"], stdin=p1.stdout, stdout=subprocess.PIPE)
        output = p2.communicate()[0]
    except AttributeError:
        print("ABORTING READ; FILE ERROR; FIXME")

    # inserts is the read specific sequence that replaces the X*8 repeats in the lab adapter
    # more specific var name TBD
    inserts = re.search('([ATCG]{5,8})', output) # TODO: more stringent regex

    if inserts:  # TODO: one or both? O|1
        p1.kill()
        p2.stdout.close()
        return pre_adapter.replace("XXXXXXXX", inserts.group(read_num))  # TODO: FIXME

    return None


def run(infile, outfile="/dev/null", params=None, lab_adapt_override=None):
    """
    single run read
    params: override given
    """
    # TODO improve redirect of standard output
    # TODO diff log files
    # TODO: implement param override
    if type(params) is str:
        params = params.split()

    # DO CHECKS
    read_num = 0 if re.search('R1', infile) else 1

    if lab_adapt_override is None:  # pythonic?
        pre_adapter = Adapters.lab0 if read_num == 0 else Adapters.lab1

    adapter = get_adapter(infile, pre_adapter, read_num) #str(adapter)]
    #print("\n\n" + adapter)
    params = ['-a', adapter]

    #with temporary_path(outfile) as tmp_fastaq: # IMPLEMENTED FOR TESTING, can remove
    params += ['-o', outfile ] # TODO parallelizable?
    params += [datapath(infile)]

        # TODO: add infile2
    with Capturing() as output:
        cutadapt.main(params)
        return output


def run_paired(infile0, infile1, tmpfile=None, tmpfile1=None, params=None):
    # TODO: implement param override
    if type(params) is str:
        params = params.split()
        #params += ['-o', p0, '-p', p1]
        #params += [datapath(in0), datapath(in1)]
    output0 = run(infile0)
    print(output0)
    output1 = run(infile1)
    return grep_report(output0, output1)

# TODO: more sophisticated regex....
# TODO: MAKE THIS FUNCTION BETTER
def grep_report(report0, report1=None):
    found0 = filter(lambda x: 'Reads with adapters:' in x, report0)  # FIXME
    if report1:
        found1 = filter(lambda x: 'Reads with adapters:' in x, report1)  # FIXME
        return found0[0].strip().join(found1[0].strip())

    return found0[0].strip()


if __name__=='__main__':
    #print(grep_report(run("R1.fastq.gz")))
    print(run_paired("R1.fastq.gz", "R2.fastq.gz"))