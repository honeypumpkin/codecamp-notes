# CodeCamp Notes

**Lesson notes for CodeCamp**

## Lesson 3
*Debugging*

### There are 3 types of errors that can occur:
1. syntax errors
2. runtime errors
3. semantic errors

#### Syntax Errors
Syntax refers to the structure of a program and the rules about that structure.
ie. forgetting a semicolon or closing a parens

*example* 
```python
print("Syntax errors are from missing bits)
```

#### Runtime Errors
These are also called exceptions as they indicate something exceptional (bad) has happened.

*example*
```python
print(6 / 0)
```

#### Semantic Errors
If there is a semantic error in your program, it will run successfully in the sense that the computer will not generate any error messages. However, your program will not do the right thing. It will do something else. Specifically, it will do what you told it to do.

*example*
```python
percent = 15
print("15% of 100 is " , percent)
```
we forgot to divide by 100 before having the percentage amount

### Avoid having to debug
1. Start small

... Run your code as you are writing it - every 2 lines will help you isolate bugs as they are introduced.

2. Keep it working 

... Once you have a working program, add small bits at a time to keep it working. If you introduce a bug you are able to isolate where it was added.