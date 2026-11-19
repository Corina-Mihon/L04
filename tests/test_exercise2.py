import os
import sqlite3
import subprocess

import pytest

import exercise2
from exercise2 import *


# bug report 1
def test_r1_clamp():
    """Test that clamp correctly limits x between low and high."""
    # Given: x=10, low=5, high=15
    # Expected: 10 (since 5 <= 10 <= 15)
    # Current code returns max(5, min(10, 5)) = max(5, 5) = 5 → incorrect
    # Fixed code should return max(5, min(10, 15)) = max(5, 10) = 10 → correct
    
    result = clamp(10, 5, 15)
    assert result == 10, f"Expected 10, got {result}"
    
    # Additional test: x below low
    result = clamp(3, 5, 15)
    assert result == 5, f"Expected 5, got {result}"
    
    # Additional test: x above high
    result = clamp(20, 5, 15)
    assert result == 15, f"Expected 15, got {result}"
    
    # Additional test: x within range
    result = clamp(10, 10, 20)
    assert result == 10, f"Expected 10, got {result}"
    
    # Test edge case: x == low
    result = clamp(5, 5, 10)
    assert result == 5, f"Expected 5, got {result}"
    
    # Test edge case: x == high
    result = clamp(15, 5, 15)
    assert result == 15, f"Expected 15, got {result}"


# bug report 2
def test_r2_is_passing_with_grade_5():
    """Test that is_passing returns True when grade is 5, as per docstring."""
    assert is_passing(5) == True, "Grade 5 should return True as it is '5 or more'"


# bug report 3
def test_r3_valid_password_length_eight():
    """Test that a password with exactly 8 characters and one digit is considered valid."""
    # Input: "pass123" has length 8 and contains a digit
    # According to the docstring, it should be valid (at least 8 characters and at least one digit)
    # Current code incorrectly returns False for this case
    result = is_valid_password("pass123")
    assert result is True, f"Expected True for password 'pass123' (length 8), but got {result}"
