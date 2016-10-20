#PUT ADAPTERS HERE FOR OTHER MODULES 

class Reports:
    trim_field = 'Reads with adapters:'
    dimer_field = 'Reads with adapters:'

class Adapters:
    lab0 = "AATGATACGGCGACCACCGAGATCTACACXXXXXXXXACACTCTTTCCCTACACGACGCTCTTCCGATCT"
    lab1 = "GATCGGAAGAGCACACGTCTGAACTCCAGTCACXXXXXXXXATCTCGTATGCCGTCTTCTGCTTG"
    insert_re = '([ATCG]{5,8})'
    replace = "XXXXXXXX"
