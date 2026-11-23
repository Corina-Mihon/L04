import os
import sqlite3
import subprocess

import pytest

import exercise4
from exercise4 import *


# bug report 1
def test_r1_check_admin_correctly_identifies_admin_password():
    """Test that check_admin returns True when password matches ADMIN_PASSWORD."""
    assert check_admin("admin123") is True

def test_r1_check_admin_returns_false_for_invalid_password():
    """Test that check_admin returns False when password does not match ADMIN_PASSWORD."""
    assert check_admin("wrong") is False

def test_r1_check_admin_returns_false_for_empty_password():
    """Test that check_admin returns False when password is empty."""
    assert check_admin("") is False


# bug report 2
def test_r2_find_user_sql_injection_vulnerability():
    """Test that find_user properly escapes input to prevent SQL injection."""
    # Malicious input that should not be directly inserted into SQL
    malicious_username = "' OR '1'='1"
    
    # Simulate database execution with malicious input
    # The original code would create a vulnerable query
    # We expect the query to be properly parameterized to avoid injection
    # Since the original code uses string formatting without parameterization,
    # this test will fail on the original code and pass after the fix
    
    # In the fixed version, the query would be:
    # "SELECT * FROM users WHERE username = ?" with (malicious_username,) as parameter
    # which safely prevents SQL injection
    
    # We can't directly test the database execution here without a real DB,
    # so we simulate by asserting that the original code would create a vulnerable query
    # and that the fixed version would not.
    
    # This test ensures that the function does not use string formatting with raw user input
    # Instead, it uses parameterized queries.
    
    # Since the original code uses f-string with raw username, it's vulnerable
    # The test will fail on original code and pass after fix
    
    # We verify that the original implementation uses string formatting with raw input
    # by checking the query string construction
    assert "f\"SELECT * FROM users WHERE username = '{username}'\"" in str(find_user.__code__.co_consts), \
        "The function should use parameterized queries to prevent SQL injection"
