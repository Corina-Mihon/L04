# Bug reports for exercise2.py

Line: 13  
Problem: The function `clamp(x, low, high)` incorrectly uses `min(x, low)` and then applies `max(low, ...)` which results in a logical error. It should clamp `x` between `low` and `high`, but the current code uses `low` twice and does not use `high` at all. Specifically, `min(x, low)` will return `x` if `x < low`, otherwise `low`. Then `max(low, ...)` will just return `low` if the previous result is `low`, which means the upper bound `high` is completely ignored.  
Example:  
Input: x=10, low=5, high=15  
Actual result: max(5, min(10, 5)) = max(5, 5) = 5  
Expected result: 10 (since 5 ≤ 10 ≤ 15)  
Fix:  
Line 13: `return max(low, min(x, high))`

Line: 2  
Problem: The docstring says "True if the grade is 5 or more", which means grades ≥ 5 should return True. However, the function uses `grade > 5`, which means grades like 5 will return False, violating the docstring.  
Example:  
Input: grade = 5  
Actual result: False  
Expected result: True  
Fix:  
Line 2: `return grade >= 5`

Line: 8  
Problem: The docstring states "At least 8 characters and at least one digit". The current code uses `len(password) > 8`, which means it requires more than 8 characters (i.e., 9 or more), not at least 8. This is a mismatch with the docstring.  
Example:  
Input: password = "pass1234" (length 9)  
Actual result: True (correct)  
Input: password = "pass123" (length 8)  
Actual result: False (incorrect — should be True)  
Expected result: True  
Fix:  
Line 8: `return len(password) >= 8 and any(c.isdigit() for c in password)`
