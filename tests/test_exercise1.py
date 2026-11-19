import os
import sqlite3
import subprocess

import pytest

import exercise1
from exercise1 import *


# bug report 1
def test_r1_is_even():
    """Test that is_even returns True for even numbers and False for odd numbers."""
    # Test case: input 4 (even) should return True
    assert is_even(4) == True, "Even number 4 should return True"
    
    # Test case: input 5 (odd) should return False
    assert is_even(5) == False, "Odd number 5 should return False"
    
    # Test case: input 0 (even) should return True
    assert is_even(0) == True, "Even number 0 should return True"
    
    # Test case: input 2 (even) should return True
    assert is_even(2) == True, "Even number 2 should return True"
    
    # Test case: input 1 (odd) should return False
    assert is_even(1) == False, "Odd number 1 should return False"


# bug report 2
def test_r2_rectangle_area():
    """Test that rectangle_area calculates area as width * height, not width + height."""
    # Given width=5, height=3
    # Expected area = 5 * 3 = 15
    # Current implementation returns 5 + 3 = 8 (incorrect)
    result = rectangle_area(5, 3)
    assert result == 15, f"Expected 15, but got {result}"


# bug report 3
def test_r3_double_function():
    """Test that double(n) returns twice the number, not n + 2."""
    assert double(5) == 10, "double(5) should return 10, but returns 7"
