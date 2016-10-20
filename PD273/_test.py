import subprocess

def run_example():
    p1 = subprocess.Popen(["zcat", "R1.fastq.gz"], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["head", "-n", "4"], stdin=p1.stdout, stdout=subprocess.PIPE)
    p3 = subprocess.Popen(["cutadapt", "-a", adapter, "-o", "/dev/null", "-"], stdin=p2.stdout)
