"""
setupDemo.py
Demo of setUp and tearDown
Unittest - demo only
"""

import unittest
import tempfile
import shutil
import glob
import os

class FileTest(unittest.TestCase):
    
    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("testdir")
        os.chdir(self.dirname)
        
    def test_1(self):
        fileSet = ['this.txt', 'that.txt', 'the_other.txt']     # make a test set
        "Verify creation of files is possible"
        for filename in ("this.txt", "that.txt", "the_other.txt"):
            f = open(filename, "w")
            f.write("Some text\n")
            f.close()
            self.assertTrue(f.closed)
        dirSet = os.listdir()                                   # get dir files for comparison
        self.assertEqual(sorted(fileSet), sorted(dirSet), "There are files present NOT from the for loop")
            
    def test_2(self):
        "Verify that the current directory is empty"
        self.assertEqual(glob.glob("*"), [], "Directory not empty")
        
    def test_3(self):
        "Create binary file with 1 million bytes"
        f = open("binary_file.txt", "wb")   # open in write binary mode
        f.write(b'1' * 1000000)             # write 1000000 ones to the file then close
        f.close()        
        self.assertEqual(os.stat("binary_file.txt").st_size, 1000000, "File size not 1 million bytes")
        
        
        
    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)
        
if __name__ == "__main__":
    unittest.main()
