import unittest
import extensions
import shutil
import os

PATHSTEM = "v:\\workspace\\FileHandling_Homework\\Tmp\\"

class TestExtensions(unittest.TestCase):
    
    def setUp(self):
        """Set up a temp dir and populate that dir
        with a hand full of files of various extensions.
        """
        os.mkdir(PATHSTEM)
        os.chdir(PATHSTEM)
        self.file_names = ["thing1.txt", "thing2.txt", "thing3.txt",
            "snake1.py", "snake2.py",
            "camel1.pl", "camel2.pl"]
        for fn in self.file_names:
            f = open(fn, "w")
            f.close()
    
    def testCount(self):
        """
        Run test to compare the number of exts in current dir
        to that of expected values
        """
        expected = {'txt': 3, 'pl': 2, 'py': 2}
        exts = extensions.getExtensions()
        self.assertEqual(exts, expected, "The extension counts do NOT match the directory")
    
    def tearDown(self):
        """Change the directory one level up,
        then delete the temp directory
        """
        os.chdir("v:\\workspace\\FileHandling_Homework\\")
        shutil.rmtree(PATHSTEM)

if __name__ == "__main__":
    unittest.main()
