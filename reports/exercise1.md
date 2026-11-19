# Bug reports for exercise1.py

Line: 3  
Problem: The condition `n % 2 == 1` checks if a number is odd, not even. For even numbers, the remainder when divided by 2 should be 0, not 1. Thus, the function incorrectly returns `True` for odd numbers and `False` for even numbers.  
Example: input: 4, actual result: False, expected result: True  
Fix: return n % 2 == 0  

---

Line: 8  
Problem: The function calculates the sum of width and height, not the area of a rectangle. The area of a rectangle is width multiplied by height, not added.  
Example: input: width=5, height=3, actual result: 8, expected result: 15  
Fix: return width * height  

---

Line: 13  
Problem: The function `double(n)` is supposed to return twice the number, but it adds 2 instead of multiplying by 2. This results in incorrect output.  
Example: input: 5, actual result: 7, expected result: 10  
Fix: return n * 2
