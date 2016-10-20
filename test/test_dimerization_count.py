import unittest
import os, sys

curr_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(curr_dir, '../src')))

from config import Adapters
import cutadapt_wrapper
class TestCutMethods(unittest.TestCase):
    def test_get_adapter(self):
        # pre_adapter = "AATGATACGGCGACCACCGAGATCTACACXXXXXXXXACACTCTTTCCCTACACGACGCTCTTCCGATCT"
        expected = "AATGATACGGCGACCACCGAGATCTACACCAGTCTGGACACTCTTTCCCTACACGACGCTCTTCCGATCT"
        adapter = cutadapt_wrapper.get_adapter('./data/test.fastq.gz', adapter, 0)

        self.assertEqual(expected, adapter)

    def test_run(self):
        pass
    def test_run_paired(self):
        pass


suite = unittest.TestLoader().loadTestsFromTestCase(TestCutMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
