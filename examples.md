# Chapter 6
Exercises
6. Write a function findHypot. The function will be given the length of two sides of a right-angled triangle and it should return the length of the hypotenuse. (Hint: x ** 0.5 will return the square root, or use sqrt from the math module)
```python
from test import testEqual

import math

def findHypot(a,b):
    c = (a**2 + b**2) ** 0.5
    return c
    
print(findHypot(9.0, 18.0))

testEqual(findHypot(12.0, 5.0), 13.0)
testEqual(findHypot(14.0, 48.0), 50.0)
testEqual(findHypot(21.0, 72.0), 75.0)
testEqual(findHypot(1, 1.73205), 1.999999)
```
![passed](figs/Ch6Num6.png)