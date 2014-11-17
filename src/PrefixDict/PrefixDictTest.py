'''
Created on 17.11.2014

@author: schnober
'''

import unittest

from PrefixDict import PrefixDict


class Test(unittest.TestCase):
    def setUp(self):
        testDict = {"test1": 4, "test2": 2, "abc": 1, "aec": 2}
        self.pd = PrefixDict(testDict)
        
    def testPrefix(self):
        self.assertEqual(6, self.pd.getPrefixEntries("t"))
        self.assertEqual(0, self.pd.getPrefixEntries("def"))
        self.assertEqual(3, self.pd.getPrefixEntries("a"))

    def testRegex(self):
        self.assertEqual(6, self.pd.getRegexEntries("^t.*[0-9]$"))
        self.assertEqual(0, self.pd.getRegexEntries("^t.*[0-9]xy"))
        self.assertEqual(3, self.pd.getRegexEntries("a.c"))
        self.assertEqual(2, self.pd.getRegexEntries("test2"))

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testPrefix']
    unittest.main()
