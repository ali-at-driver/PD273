"""
PD-274: Count number of reads with some adapter sequence identified/removed

BELOW ARE PLACEHOLDERS TO BE ALTERED
"""
import argparse
import cutadapt_wrapper
from config import Reports
import enqueue_files
import multiprocessing

def grep_report(report0, report1=None):    
    """
    Overview of removed sequences
    lengthcountexpectmax.errerror counts
    31615.6016
    433.903
    """
    # FIXME: below are just placeholders
    print(grep_report_helper(report0))
        # TODO: perform re.search for values and populate csv(?) some kind of output dependent on pipeline needs
    if report1:
        print(grep_report_helper(report1))


def grep_report_helper(report):
    final_report = ""
    idx = report.index(Reports.dimer_field)
    for i in xrange(idx, len(report)):
        final_report += report[i]
        final_report += "\n"
    return final_report


def mp_worker((file1, file2)):
    output0, output1 = cutadapt_wrapper.run_paired(file1, file2)
    grep_report(output0, output1)


def mp_handler(data):
    p = multiprocessing.Pool(2)
    p.map(mp_worker, data)


if __name__=='__main__':
    #outputs = cutadapt_wrapper.run_paired("data/R1.fastq.gz", "data/R2.fastq.gz")
    #grep_report(outputs[0], outputs[1])
    data = enqueue_files.pair_files('./data')
    mp_handler(data)
