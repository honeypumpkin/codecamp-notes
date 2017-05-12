# CHAPTER 6 - CONDITIONALS

## Making Decisions with Conditionals

Consider the follwoing real-world instructions:

*Go to the grocery store. If they have bananas, buy them. If they are out of bananas, buy apples.*

## Making decisions with code
*ask user for integer, if even print wiz, if odd print bang*
```python
user_input = int(input("Enter an integer"))
# can't really do much more then that
```

## Branching
We want our code to be able to flow 
```
--> condition

    true --> code block #1

    false --> code block #2
```

## Booleans
Booleans are special data types (bool in Python) that signify True and False.
They:
* must be captialized
* are not strings; True is different then "True"
* are the result of certain arithmetic comparison expressions
``` python
print(type(True))
```
**Output**: `<class 'bool'>`

## Comparisons
For numbers (integers or floats) we can use **comparison operators** which evaluate to booleans:
-  '>' (greater than)
-  '>= (greater than or equal to)
-  < (less than)
-  <= (less than or equal to)
-  ==  (equal to)*
-  != (not equal to) 

## Comparison examples

``` python
8 > 7 # True
8 < 7 # False
```

## Boolean jAlgebra
We can combine boolean values in wasy using `and`, `or` and `not` that match our natural language usage of combining different conditions.

* Example 1:
It is Friday and we are in class
* Example 2:
I am awake or I am asleep
* Example 3: The sky is not green

``` python
x = 5
y = 6

print(x < 10 and y < 10) #True
print(x == 5 or y == 5) #True (If one statement is true, the entire statement is true)
print(not x > y) #True (sneaky)
```

## Conditional Syntax
Anatomy of a conditional:

``` python
if <condition>:
    #code block #1
else:
    #code block #2
```
* *condition*: a test. this is something that is eather `True` or `False`
* *code block #1*: if the condition is `True`, this code executes
* *code block #2*: if code block #1 condition is `False`, code block #2 executes.
* *indents*: the code blocks are indented once to tell python that they are part of the `if` or `else` condition.

**Book Examples:**
```python
user_input = int(input("Give me an integer"))
if user_input % 3 == 0:
    print("is a multiple of 3")
else:
    print("not a multiple of 3")
```
## The `else` clause
We can omit the `else` portion of a conditional
```python
user_input = int(input("Give me an integer"))
if user_input > 100:
    print("wow that is a big number")
```
### Nesting conditionals
We can nest conditionals, but must use multiple levels of indentation.
```python
if n < 0:
    print("blah")
else:
    if n > 0:
        print("blah blah")
    else:
        print("blah blah blah")
```

## The `elif` clause
We can have multiple branches -- that is, multiple tests -- within the same condtional using `elif`
```python
if n < 0:
    print("blah")
elif n > 0:
    print("blah")
else:
    print("blah")        
```

print statements will only print the first function that is true. so if first conditional is true, that one will be printed.

```python
n = 5
if n < 10:
    print("less")
elif n < 8:
    print("less less")
elif n < 6:
    print("less less less")
```
This will only print `less`
