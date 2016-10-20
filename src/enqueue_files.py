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
        # FIXME....formalize path 
        name1 = path + name[0] + 'R1' + name[1]
        name2 = path + name[0] + 'R2' + name[1]
        paired_fnames.append([name1, name2])
    return paired_fnames
