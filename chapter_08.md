* slice operator: basically allows you to pick parts of a string and return them.
    * bracket notation: `my_list[i], my_str[j]`
    * `my_str[i:j],` eg.

* immutability: One final thing that makes strings different from some other Python collection types is that you are not allowed to modify the individual characters in the collection
    * `greeting = "Hello, world!"`
    * `greeting[0] = 'J'            # ERROR!`
    * `print(greeting)`
    * the way to do this is to actually create a new string.
    ```python
    my_str = 'orange'
    new_str = ''

    for i in range(len(my_str)):
        if i == 0
            new_str =+ 'g'
        else:
            new_str += my_str[i]
    print(new_str)
    print('g' + my_str[1:]) 
    #with this we don't need the for loop!
    ```
* find: search a string for a char and get it's location.
    * `my_str.find('n')` is going to find the 'n' in my string and return it's location

## examples
`while` loop
___
```python
is_input_valid = False

while not is_input_valid:
    radius = input("What is the radius?")
    
    if not radius.isnumeric():
        print("thats not a number, try again")
    else:
        is_input_valid = True
        radius = int(radius)
        
print(3.14 * radius **2)
```

4. 
```python
from test import testEqual

def remove(substr,theStr):
    loc = theStr.find(substr)
    if loc!= -1:
        theStr = theStr[:loc] + theStr[loc + len(substr):]
        
    return theStr

testEqual(remove('an', 'banana'), 'bana')
testEqual(remove('cyc', 'bicycle'), 'bile')
testEqual(remove('iss', 'Mississippi'), 'Missippi')
testEqual(remove('egg', 'bicycle'), 'bicycle')
testEqual(remove('oo', 'Yahoohoo'), 'Yahhoo')
```

5. Instead of removing the first instance, remove all instances. Modified #4 code...
```python
from test import testEqual

def remove_all(substr,theStr):
    loc = theStr.find(substr)
    
    while loc!= -1:
        theStr = theStr[:loc] + theStr[loc + len(substr):] #when in doubt draw it out!
        loc = theStr.find(substr)
        
    return theStr

testEqual(remove_all('an', 'banana'), 'ba')
testEqual(remove_all('cyc', 'bicycle'), 'bile')
testEqual(remove_all('iss', 'Mississippi'), 'Mippi')
testEqual(remove_all('eggs', 'bicycle'), 'bicycle')
```