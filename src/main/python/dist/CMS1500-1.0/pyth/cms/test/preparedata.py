'''
Created on Dec 2, 2016

@author: Venkatesh
'''
import unittest

from pyth.cms.dao.TestData import prepareData
from pyth.cms.properties import appProperties_stub as appProp


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        b = prepareData(appProp)
        for b1 in b:
            print b1


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()