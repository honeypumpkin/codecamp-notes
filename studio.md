# 6. Sorted

## Walkthrough
Write a function `remove_char` that takes two string arguments, `a_str` and `a_char`. The first argument should be a string and the second should be a character (i.e. a string of length one). The function should return a new string, the result of which is `a_str` with each instance of `a_char` removed.

```python
from test import testEqual

def remove_char(a_str, a_char):

    #create new string
    new_str = ''
    
    # loop through and copy characters to new string
    
    for char in a_str:
        if char != a_char: 
        #this makes sure you only copy the chars NOT given
            new_str += char 
            #this is what copies the chars
    
    return new_str 
    #returns new string with copied chars

print(remove_char('donkey', 'k'))

testEqual(remove_char('aardvark', 'a'), 'rdvrk')
testEqual(remove_char('aardvark', 'k'), 'aardvar')
testEqual(remove_char('asdf', 'z'), 'asdf')
testEqual(remove_char('', 'a'), '')
```
### USING THE INDEX
```python
from test import testEqual

def remove_char(a_str, a_char):

    #create new string
    new_str = ''
    
    # loop through and copy characters to new string
    
    #for char in a_str:
    for idx in range(len(a_str)):
        
        #if char != a_char: 
        if a_str[idx] != a_char: 
        #this will pull each char out one at a time 
        #NOTE THIS IS THE INDEX OPERATOR NOT THE INDEX METHOD
        
            #new_str += char 
            new_str += a_str[idx]
    
    return new_str #returns new string with copied chars
    
print(remove_char('donkey', 'k'))
      
testEqual(remove_char('aardvark', 'a'), 'rdvrk')
testEqual(remove_char('aardvark', 'k'), 'aardvar')
testEqual(remove_char('asdf', 'z'), 'asdf')
testEqual(remove_char('', 'a'), '')
```
### Write a function that will use `idx` to print the location and the letter.
```python
def str_indexes(a_str):
    for idx in range(len(a_str)): #loops for length (len) of string
        print(str(idx) + ': ' + a_str[idx])
        
str_indexes('coding is fun')   
```
![example](figs/idx_example.png)
___

## Studio 
Since a string is just a sequence of characters, they can be sorted from least to greatest. Sorting can be hard so we’re just going to check if a string is sorted. Write a function which returns a boolean indicating if the string is sorted or not.

Here’s an example of how your function should behave. (Recall that the order operators are case-sensitive, so that `"A" < "a"` evaluates to `True`.)
```python
is_sorted("ABC") == True
is_sorted("aBc") == False
is_sorted("dog") == False
```
*Restate the problem*
* verify the string is sorted

*Break it down*
* verify = return Boolean
* sorted = lexicographically (caps are < lowercase)

*Figure our tools needed*
```python
# look left to right:
    #look at each pair
#1st 'A' < 'B' returns TRUE
#2nd 'B' < 'C' returns TRUE
#3rd NONE - only need a 2-loop 
def is_sorted(string):
    """Returns True if string is sorted from least to greatest
       False otherwise.
    """
    
    for idx in range(len(string)):
        
        if string[0] < string[1]:
            if string[1] < string[2]:
                return True
        else:
            return False

print(is_sorted('ABC'))
print(is_sorted('aBc'))
print(is_sorted('dog'))
print(is_sorted('Cat')) 
```  
*Key Questions*
* How many times should I loop?
* How to keep track or properly return the answer?
* Each time through the loop how do I get a pair of adjacent letters? (*HINT: use `idx`*)

Answer:
```python
def is_sorted(string):
  
    for i in range(len(string)-1):
        
        if not string[i] <= string[i+1]:
            return False
        else:
            return True
```

# 10. counting Characters

## Walkthrough

Write a “gradebook” program that takes grade data for a student and prints the resulting GPA. The output should look something like this:
``` python
Your grade (0.0-4.0): 4
# credits: 3
Enter another grade? [y/n]: y
Your grade (0.0-4.0): 4
# credits: 2
Enter another grade? [y/n]: n
Your GPA is: 4.0
```
to calculate gpa:
* GPA = QS/Total credits
* QS = sume of each credit * score

What to do ?

1. going to need to create a list to hold grades
1. 


