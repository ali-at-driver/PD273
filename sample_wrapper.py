from multiprocessing import Process, Queue
import argparse
import sys

def Worker(Process):
    # param override
    def __init__(self, inf0, inf1, queue=None, results=None):
        self.infile0 = inf0
        self.infile1 = inf1
        self.queue = queue
        self.results = results


class Writer(Process):
    def __init__(self, queue=None, trimmed=None, outfile=None):
        super(Writer, self).__init__()
        self.queue = queue
        self.trimmed = trimmed
        self.outfile = outfile

    def run(self):
        get_func = self.queue.get
        reads = get_func()
        with self.outfile as outfile:
            kept = 0
            while reads is not None:
                for read in reads:
                    outfile.write(read)
                    kept += 1
                reads = get_func()
        self.trimmed.put(kept)
