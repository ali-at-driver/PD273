#PUT ADAPTERS HERE FOR OTHER MODULES 

class Reports:
    trim_field = 'Reads with adapters:'
    dimer_field = 'Overview of removed sequences'

class Adapters:
    lab0 = "AATGATACGGCGACCACCGAGATCTACACXXXXXXXXACACTCTTTCCCTACACGACGCTCTTCCGATCT"
    lab1 = "GATCGGAAGAGCACACGTCTGAACTCCAGTCACXXXXXXXXATCTCGTATGCCGTCTTCTGCTTG"
    insert_re = '([ATCG]{5,8})'
    replace = "XXXXXXXX"
