import subprocess

import sys
from multiprocessing import Process, Queue


class Worker(Process):
    def __init__(self, infile, adapter, head=True, limit=40, outfile=None, gunzip=False):
        super(Worker, self).__init__()
        self.infile = infile
        self.adapter = adapter

        self.head = head
        self.limit = limit

        self.stdout = outfile if outfile else "/dev/null"
        self.gunzip = "gunzip" if gunzip else "zcat"

    def check_fname():
        return False
    
    def sub_adapter():
        return False

    def run_example():
        p1 = subprocess.Popen([self.unzip, self.fname], stdout=subprocess.PIPE)
        if self.head:
            p2 = subprocess.Popen(["head", "-n", self.limit], stdin=p1.stdout, stdout=subprocess.PIPE)
            p3 = subprocess.Popen(["cutadapt", "-a", self.adapter, "-o", "/dev/null", "-"], stdin=p2.stdout)
        else:
            p2 = subprocess.Popen(["cutadapt", "-a", adapter, "-o", "/dev/null", "-"], stdin=p2.stdout)

thread = Worker(threadID=1, fname="thread 1")

thread.start()

def main():
    workers = []
    def start_workers():
        for i in xrange(threads):
            worker = Worker
        
        
