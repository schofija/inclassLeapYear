import leapYear
import pytest
import unittest
#----------------------------
# Test file for leapYear.py
# Author: Jack Schofield
# Date: 5/22/2021
#----------------------------

#pytest functions
def test_leapYear1():
    assert leapYear.isLeapYear(2000) == 1

def test_leapYear2():
    assert leapYear.isLeapYear(2001) == 0
    
def test_leapYear3():
    assert leapYear.isLeapYear(1900) == 0
    
def test_leapYear4():
    assert leapYear.isLeapYear(2004) == 1

