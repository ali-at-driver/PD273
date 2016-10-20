import multiprocessing
import argparse
import sys
import glob
from config import Reports
import cutadapt_wrapper
from os import walk
from dimerization_count import grep_report
def get_filenames(path):
    f = []
    for (_, __, filenames) in walk(path):
        #f.extend(filenames)
        for name in filenames:
            if 'I1' in name or 'I2' in name: 
                continue
            f.append((name[:Reports.barcode_len], name[22:]))
    return set(f)

# USE FILTER OR SOMETHING 
def pair_files(path): #dict
    paired_fnames = []
    fnames = get_filenames(path)
    
    # there quite literally has to be a better way to do this
    for name in fnames:
        # FIXME
        name1 = './data/' + name[0] + 'R1' + name[1]
        name2 = './data/' + name[0] + 'R2' + name[1]
        paired_fnames.append([name1, name2])
    return paired_fnames


def mp_worker((file1, file2)):
    output0, output1 = cutadapt_wrapper.run_paired(file1, file2)
    dimerization_count.grep_report(outputs[0], outputs[1])
def mp_handler(data):
    p = multiprocessing.Pool(2)
    p.map(mp_worker, data)

#E144-T1-D1_S15_L004_I1_001.fastq.gz
#if __name__=='__main__':
#    data = pair_files('./data')
#    mp_handler(data)
