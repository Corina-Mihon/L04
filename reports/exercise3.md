# Bug reports for exercise3.py

Line: 3  
Problem: The function `average(numbers)` returns `sum(numbers) / len(numbers)`, which will raise a `ZeroDivisionError` when the input list is empty because `len(numbers)` becomes 0. The docstring states that an empty list has an average of 0, but the current code does not handle this case.  
Example:  
Input: `[]`  
Actual result: `ZeroDivisionError: division by zero`  
Expected result: `0`  
Fix:  
```python
def average(numbers):
    """Average of a list. An empty list has average 0"""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)
```

Line: 8  
Problem: The function `first_word(text)` uses `text.split()[0]`, which will raise an `IndexError` when the input text is empty (i.e., when `split()` returns an empty list). The docstring says it should return an empty string `""` if the text is empty.  
Example:  
Input: `""`  
Actual result: `IndexError: list index out of range`  
Expected result: `""`  
Fix:  
```python
def first_word(text):
    """The first word of the text, or "" if the text is empty"""
    words = text.split()
    return words[0] if words else ""
```

Line: 13  
Problem: The function `percent(part, total)` returns `part / total * 100`, which will raise a `ZeroDivisionError` when `total` is 0. The docstring explicitly states that if `total` is 0, the result should be 0.  
Example:  
Input: `part=5, total=0`  
Actual result: `ZeroDivisionError: division by zero`  
Expected result: `0`  
Fix:  
```python
def percent(part, total):
    """part as a percentage of total. If total is 0, the result is 0"""
    if total == 0:
        return 0
    return part / total * 100
```
