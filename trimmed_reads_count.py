"""
PD-274: Count number of reads with some adapter sequence identified/removed
"""
import cutadapt_wrapper
from config import Reports

def grep_report(report0, report1=None):
    found0 = filter(lambda x: Reports.trim_field in x, report0)  # FIXME
    if report1:
        found1 = filter(lambda x: Reports.trim_field in x, report1)  # FIXME
        # TODO: add filename? do this in run_paired
        return "R1 report: " + found0[0].strip()[20:] + "\tR2 report: " + found1[0].strip()[20:]  # FIXME THIS IS TERRIBLE

    return found0[0].strip()

def process_dir():
    print("do Pool and call to sample wrapper here")

if __name__=='__main__':
    print(cutadapt_wrapper.run_paired("data/R1.fastq.gz", "data/R2.fastq.gz"))
