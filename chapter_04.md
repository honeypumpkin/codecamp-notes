# Chapter 4 - Loops and Turtles

## I. LOOPS
___

### A. Repeating a task
Consider the following problem: 
**Print out all of the integers from 1 to 100**
One possible solution-
``` python
print (1)
print (2)
# ... and so on
```
This is tedious and not the way to do this.

### B. Loop Components
In order to repeat a task, we need two things:
1. The task that should be repeated (eg. 'Print a number')
2. The data set that shoudl be used with the task (eg. 'use 1...100')

### C. Lists
A list in Python is a data structure that allows us to collect several values in a  single variable or value.
Lists look like this:
``` python
[value1, value2, value3,..., valueN]
```
___
**NOTE:** A list holds multiple values, *HOWEVER* the list itself is a single value
___

List Examples:
``` python
[1, 2, 3, 4, 5]
["apple", "orange", "banana"]
#homogenius lists
[36, True, "eggs", 2.7]
#multiple value list
```

#### 1. Lists as types and values
We can store a list in a variable:
``` python
retired_nums = [1, 2, 6, 9, 10]
```
Lists define a new data type:
``` python
print(type(retired_nums))
```
**Output**
<type 'list'>

#### 2. For loops
A `for` loop allows us to repeat a section of code a specific number of times.
Each `for` loop has an iterator variable 

``` python
for name in ['Jesse', 'Sally', 'Zack', 'Chris']:
# /name/ is variable iterator     list      colon
    print(name)
    # loop body using variable iterator
```
___
**Note:** 
*Variable iterator*: takes on each value of the list, one at a time
*Loop body*: indeted and executed once per item in the list
___

*Examples*

``` python
some_numbers = [15, 16, 35, 98]
sum_of_numbers = 0
for number in some_numbers:
    sum_of_numbers = sum_of_numbers + number
    print(number)
    #indented defines the loop bosy

print("Sum:", sum_of_numbers)
#notice not indented. This shows the loop is over.
```

Ok - back to initial problem: 
**Print out all of the integers from 1 to 100**
``` python
print (1)
print (2)
# ... and so on
```
Still tedious with a loop
``` python
some_numbers = [1, 2, 3...]
```
### D. The `range` Function

The function `range(n)` will create a list of `n` integers from `0` to `n-1`
```python
print(range(5))
```
**Output** `[0, 1, 2, 3...]`
___
**NOTE:**
Python always prints from `0`
___

*Example*
```python
for number in range(50)
    print(number)
```
#### Using the `range` Function
To create more custom/complicated lists, use:
```python
range(start, stop, step)
```
* Start (your starting number)
* Stop (usually +/- 1 from the actual number)
* Step (how many by each step; can use -(number) to count backwards; can leave off step and just step by 1 default)
___
## II. TURTLES
___
### A. What is a turtle?
A turtle is a visual queue that will draw patters on the screen based on commands given.
We'll use a Python **module** called `turtle` that will give us a nice way to build simple images using loops.

`import turtle` makes the `turtle` module available within our program

`sam = turtle.Turtle()` creates the turtle and names it

`sam.forward(150)` commands sam to move 150 px in the initial direction. 
___
**NOTE:** Turtles always start in the center facing right, unless you designate starting point
___
`sam.left(90)` turns the turtle 

`sam.forward(150)` moves sam again

... and on and on

---
**NOTE:** code repeats... 
* **D**on't
* **R**epeat
* **Y**ourself
___
since you are using the same turn should creat a loop with moving and turning.

```python
import turtle
zack = turtle.Turtle()
side_lenght = 50
for side in range(4)
    zack.forward(sidelenght)
    zack.left(90)
```
___
### B.  Turtle methods
Don't forget to put `name`. before your method!

![turtles](figs/turtles.png)
___

## III. Function Usage

Each function that we have used has taken one or more parameters.
```python

```

Int these three examples, the parameters are:
* 'Hello World'
* 'What's your name?'
* range(1, 5, 12)
___
### A. Functions that return values
of the functions we've used, `input` and `range` result in a vlue being given back to us. This value is known as a **return value**.
```python

```
___
### B. Defining a function
We can define our own functions with the following syntax:
```python
def my_function(parameters):
#function code, with or without a return value
```
We can call the functions we define the same way that we call other functions.
#### *Hello, world function*
```python
def hello_world():
    return "Hello, world"

message = hello_world()
print(message)
```
**Output**: `Hello world`

#### *Hello, world funciton with parameter*
```python
def hello_wold(name):
    return "Hello " + name

message = hello_world("Sally")
print(message)
```
**Output**: `Hello Sally`
___

## MODULES

### A. What is a module?
A **Python module** is a collection of Python code that is bundled for others to use, but which is NOT part of the core Python programming language.

To use modules, we must *install* and then *import* them.
___
### B. Modules in Activecode/Runestone
Within the editors in the online textbook, the only modules available are:
1. `turtle`
2. `math`
3. `random`
___
### C. Modules in "Real Coding Environments
Installing a module requires a program like `pip` or `conda`. We'll use both in this class.
```bash
$ conda install pytest
```
```bash
$ pip install pytest-html
```
These tools will install and manage modules on your computer in different ways. Each has an online repository of modules that are available to install with the given tool.
___
### D. Package repositories
There are many repositories for Python. 
Pip
`pip` installs packages from Python 
___
### E. Using Modules
For a module that is available it can be used within a program by importing the module
```python
import math
```
The identifier `math` is now available for us to use within our file.
```python
print(math.pi)
```
**Output**: `3.1415926535589793...`
___
### F. Modules we will be using

1. The `math` Module: This module provides math-related utilities
* 
* 

2. The `random` Module: This module provides utility functions for generating random numbers.
    
* `random.random()` -returns a random float between 0 and 1
* `random.randrange(n, m)` -returns a random integer between `n` and `m`-1.

    ___
    **NOTE:** When a computer scientist says "random number" they usually mean a *pseudo-random* number. An Algorithm can't generate *truly* random numbers.
    ___
*Examples*

```python
import random
#generate a random float between 1 and 5
num = random.random()
num = num * 4  #This will give us a number between 0-4
num = num + 1  #This will SHIFT the set over by 1, so now a number between 1-5
print(num)
```
```python
import random
#generate a random integer between 32 and 212
num = random.randrange(32, 213)
print(num)
```

*For help with math and randome functions, check out the Python standard library:*
https://docs.python.org/3/library/math

___
## PYTHON AT THE COMMAND LINE
```terminal
$ python
>>> num = 5
>>> print(num)
5
>>> 
```
You can run one line at a time, you can import random/math etc. To exit type 'exit()' or 'quit()'

### Pyton REPL
**R**e 

**E**valuate 

**P**rint 

**L**oop




