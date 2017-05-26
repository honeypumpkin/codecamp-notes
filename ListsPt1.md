# Lists pt 1

## LIsts as ordered collections
* Like strings, lists are a **collection data type**
* This also means they are non-primitive, or that they contain...
* A list may contain any value. Really, Any value. This means we can do things like: 
``` python 
mixed_list = [1, 2, [3, 4]]
```
* here, `[3, 4]` is referred to as a sublist
___
## Stuff we can do with lists
* Get the length
```python
print(len(["a", "b", "c"]))
```
* can also use bracket notation
``` python
some_numbers['a', 'b', 'c']
number a = 0
```
* Can use the `in` operator to create boolean expressions to determine wheere or not the item is in a list
``` python
letters = ['a', 'b', 'c']
print('a' in letters)
print('b' in letters)
print('d' in letters)
```
output: 

`True`

`True`

`False`

* Can use `+` to concatenate lists
``` python
combined = ['a', 'b', 'c'] + [1, 2, 3]
print(combined)
```
output:

`['a', 'b', 'c', 1, 2, 3]`

* we can use * to repeat lists
``` python
['a', 'b', 'c'] * 3
```
output:

`'a', 'b', 'c','a', 'b', 'c','a', 'b', 'c'`
___
## Objects and References

In Python, every value is an object.
* References refer to a piece of data that lives somewhere else on the computer (Technically a 'Memory Address').

* For every unique string there will only ever be one copy of that unique string in memory. limitless variables can point to this one string.

* Every object is given a unique id (think of ssn). 

* Can use the operator `is` instead of `==` to call a boolean. must remember though that there is a difference between equality and sameness. 
    * `is` is testing for sameness (checking ids)
    * `==` is testing for value
    * this does NOT work for lists
    ``` python
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list1 is list2
    #output = `False`
    list1 == list2
    #output = `True`
    ```
* With LISTS even if the list is the same, a new object is made.

## Split/Join



