"""
PD-274: Count number of reads with some adapter sequence identified/removed

BELOW ARE PLACEHOLDERS TO BE ALTERED
"""
import argparse
import cutadapt_wrapper
from config import Reports


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


def output_log():
    print("port report to log")


def process_dir():
    print("do Pool and call to sample wrapper here")

if __name__=='__main__':
    outputs = cutadapt_wrapper.run_paired("data/R1.fastq.gz", "data/R2.fastq.gz")
    grep_report(outputs[0], outputs[1])
