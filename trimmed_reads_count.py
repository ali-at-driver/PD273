"""
PD-274: Count number of reads with some adapter sequence identified/removed
"""
import cutadapt_wrapper

if __name__=='__main__':
    print(cutadapt_wrapper.run_paired("data/R1.fastq.gz", "data/R2.fastq.gz"))
