# Chapter 4 - Loops and Turtles

### Repeating a task
Consider the following problem: 
**Print out all of the integers from 1 to 100**
One possible solution-
``` python
print (1)
print (2)
# ... and so on
```
This is tedious and not the way to do this.

### Loop Components
In order to repeat a task, we need two things:
1. The task that should be repeated (eg. 'Print a number')
2. The data set that shoudl be used with the task (eg. 'use 1...100')

### Lists
A list in Python is a data structure that allows us to collect several values in a  single variable or value.
Lists look like this:
``` python
[value1, value2, value3,..., valueN]
```
**NOTE** A list holds multiple values, *HOWEVER* the list itself is a single value

List Examples:
``` python
[1, 2, 3, 4, 5]
["apple", "orange", "banana"]
#homogenius lists
[36, True, "eggs", 2.7]
#multiple value list
```

### Lists as types and values
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

### For loops
A `for` loop allows us to repeat a section of code a specific number of times.
Each `for` loop has an iterator variable 

``` python
for name in ['Jesse', 'Sally', 'Zack', 'Chris']:
# variable iterator       list               colon
    print(name)
    # loop body
```
**Note:** 
*Variable iterator*: takes on each value of the list, one at a time
*Loop body*: indeted and executed once per item in the list





