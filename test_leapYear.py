import leapYear
import pytest
import unittest
#----------------------------
# Test file for leapYear.py
# Author: Jack Schofield
# Date: 5/22/2021
#----------------------------

#pytest functions
def test_leapYear1_py():
    assert leapYear.isLeapYear(2000) == 1

def test_leapYear2_py():
    assert leapYear.isLeapYear(2001) == 0
    
def test_leapYear3_py():
    assert leapYear.isLeapYear(1900) == 0
    
def test_leapYear4_py():
    assert leapYear.isLeapYear(2004) == 1
    
def test_leapYear5_py():
    assert leapYear.isLeapYear("asdf") == 2
    
#unittest
class test_LeapYear(unittest.TestCase):
    def test_leapYear6_ut(self):
        self.assertTrue(leapYear.isLeapYear("2000"), 2)
        
    def test_leapYear7_ut(unittest.TestCase):
        self.assertTrue(leapYear.isLeapYear(1800), 0)

