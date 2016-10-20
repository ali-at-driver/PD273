"""
PD-274: Count number of reads with some adapter sequence identified/removed
"""
import argparse
import cutadapt_wrapper
from config import Reports
import enqueue_files
import multiprocessing 

def grep_report(report0, report1=None):
    """
    BELOW IS A PLACEHOLDER
    """
    found0 = filter(lambda x: Reports.trim_field in x, report0)  # FIXME
    if report1:
        found1 = filter(lambda x: Reports.trim_field in x, report1)  # FIXME
        # TODO: add filename? do this in run_paired
        return "R1 report: " + found0[0].strip()[20:] + "\tR2 report: " + found1[0].strip()[20:]  # FIXME THIS IS TERRIBLE

    return found0[0].strip()


def mp_worker((file1, file2)):
    output0, output1 = cutadapt_wrapper.run_paired(file1, file2)
    print(grep_report(output0, output1))


def mp_handler(data):
    p = multiprocessing.Pool(2)
    p.map(mp_worker, data)

if __name__=='__main__':
    #print(cutadapt_wrapper.run_paired("data/R1.fastq.gz", "data/R2.fastq.gz"))
    data = enqueue_files.pair_files('./data/')
    mp_handler(data)
