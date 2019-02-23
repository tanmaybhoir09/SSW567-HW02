
"""
Updated Feb 22, 2019
The primary goal of this file is to demonstrate a simple unittest implementation
@author: jrr
@author: rk
@auther: Tanmay Bhoir
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right')
        
    def testEquilateralTrianglesA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral')

    def testEquilateralTrianglesB(self): 
        self.assertEqual(classifyTriangle(100,100,100),'Equilateral')

    def testIsocelesTrianglesA(self): 
        self.assertEqual(classifyTriangle(5,5,3),'Isoceles')

    def testIsocelesTrianglesB(self): 
        self.assertEqual(classifyTriangle(36,28,36),'Isoceles')

    def testScaleneTrianglesA(self): 
        self.assertEqual(classifyTriangle(13,9,14),'Scalene')

    def testScaleneTrianglesB(self): 
        self.assertEqual(classifyTriangle(7,15,12),'Scalene')

    def testNotATriangleA(self): 
        self.assertEqual(classifyTriangle(1,2,10),'NotATriangle')

    def testNotATriangleB(self): 
        self.assertEqual(classifyTriangle(150,1,1),'NotATriangle')

    def testNotATriangleC(self): 
        self.assertEqual(classifyTriangle(300,2,2),'NotATriangle')

    def testInvalidInputA(self): 
        self.assertEqual(classifyTriangle(10,False,10),'InvalidInput')

    def testInvalidInputC(self): 
        self.assertEqual(classifyTriangle(-1,-1,-1),'InvalidInput')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)