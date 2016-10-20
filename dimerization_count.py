"""
Calculate adapter dimerization read counts (full read is just adapter)
"""
import cutadapt_wrapper

def make_pool():
    return "hello world"

if __name__=='__main__':
    print(cutadapt_wrapper.run_paired("data/R1.fastq.gz", "data/R2.fastq.gz"))
