# Chapter 10

## Questions:
`What is printed by the following statements? (T/F)`

* `alist = [3, 67, "cat", [56, 57, "dog"], [ ], 3.14, False]`

* `print(57 in alist)`

How to print a sublist?

___
## Exercises
4. Write a function to count how many odd numbers are in a list.

```python
import random

def odd_num(lst):
    odd = 0
    for e in lst:
        if e % 2 != 0:
            odd = odd + 1
    return odd
        
lst = []   
for i in range(100):
    lst.append(random.randint(0, 1000))
    
print(odd_num(lst))
```
## LESSON NOTES
* *Lists* - things that we can do with them
    * `sort()`
    * access members by index using `[]`
    * get lenght using `len()`
    * `append()`
    * `insert()`
    * `pop()`
    * `remove()`
    * concatenate using `+`
    * assign a value to a given index: `my_list[3] = 'a'`
    * slice: `my_list[start:end]`
    * clone: `my_list[:]`

When we call a funciton and pass it a reference variable (eg. something that holds a list), the function can CHANGE that object - called "passing by reference"

When we call a function and pass it a primitive value, that value is copied in - "called passing by value"
