import os
import sqlite3
import subprocess

import pytest

import exercise3
from exercise3 import *


# bug report 1
def test_r1_average_empty_list():
    """Test that average returns 0 for an empty list, avoiding ZeroDivisionError."""
    result = average([])
    assert result == 0, f"Expected 0 for empty list, but got {result}"


# bug report 2
def test_r2_first_word_empty_text():
    """Test that first_word returns empty string for empty input, not IndexError"""
    result = first_word("")
    assert result == "", "Expected empty string for empty input, but got {}".format(result)


# bug report 3
def test_r3_percent_zero_division():
    """Test that percent() returns 0 when total is 0, avoiding ZeroDivisionError."""
    assert percent(5, 0) == 0
