# Lists
1. Explain what is a list in Python.
    * Lists define a data type
    * They are mutable
    * are ordered collections (dictionaries are UNORDERED collections)
        * use tuples and indexes
        * can index into lists with `[]`
1. Explain how can you find the length of a list.
    * len
1. Explain how to access elements in a list.
    * use [] with indexing...
    ```python
    langs = ['python', 'java', 'javascript', 'c#']
    third_lang = langs[2]
1. Explain how can you check if an item is in the list.
    * use boolean notation (using the `in` operator)
    ```python
    print('x' in langs)
    ``` 
1. Explain how to concatenate a list.
    * use the `+` operator
    ```python
    more_langs= langs + ['haskell', 'scala']
    ```
1. Explain how to repeat a list.
1. Explain how to slice a list.
    * slicing give many things
    * `first_two = langs[:2]` everything from the start to index 2
    * `last_two = langs[2:]`
    * `middle_two = langs[1:3]`
1. Explain what it means for lists to be mutable.
    * This means that they are editable **MORE**
1. Explain how to delete items from the list.
1. Explain how references work. (An example may help here)
    * passing by reference/aliasing /non-primitive/
    ```python
    a = [1, 2, 3]
    b = 9
    b [0] = 4
    print(a[0])
    ```
1. Explain what is aliasing.

1. Explain how to clone a list.
    * `langs_clone = langs[:]`
    * this will clone the entire list or "slice" the list into a new list.
1. Name some of the list methods. Particularly, these would be good to remember
    1. `append` (especially vs concatenation)
    2. `insert`
1. Traverse through a list with a loop.
    ```python
    for lang in langs:  #preferred method/easier
        print(lang)

    for i in range(len(langs)):  #use if you need to use the index for the particular thing your looking for
        print(langs[i])
    ```

1. Explain how lists are sent as arguments (passing by reference vs. passing by value).
    * passing by reference/aliasing /non-primitive/
    * lists, dictionaries, objects
    ```python
    def change_list(my_list):
        my_list[0] = 4

    b = [1, 2, 3]
    change_list(b)
    print(b)
    ```
    ___
    * passing by value /primitive types/
    * `int`, `float`, `bool`
    ```python
    def add_two(num):
        num = num + 2

    a = 2
    add_two(a)
    print(a)
    ```
    
1. Explain what is a pure function.
    * a function that doesn't change any arguments
    * pure function:
    ```python
    def pure_double(my_list):
        return my_list * 2
    ```
    * non-pure (mutating):
    ```python
    def mutating_double(my_list):
        for i in range(len(my_list)):
            my_list.append(my_list[i])
    ```

1. Implement a function that produces a list of items (using the accumulator style).
1. Explain what is a list comprehension.
1. Implement an example of how to access an element from nested lists.
1. Explain how the string split method works.
1. Explain what is a tuple and how they differ from lists.
1. Explain how tuple assignment works.
1. Implement a function that produces a tuple.
# Dictionaries
1. Explain what a dictionary is in Python
1. Create dictionaries with entries
1. Explain what it means to say that "dictionaries are mutable"
1. Describe the types of keys that a dictionary may have
1. Access individual elements of a dictionary
1. Modify individual elements of a dictionary
1. Loop through the elements of a dictionary
1. Use dictionary methods such as keys(), values(), and get()
# Objects
1. Explain what an object is. In particular, what does an object contain?
1. Write your own user defined class.
1. Explain what an initializer method is.
1. Explain what is a class vs an instance.
1. Explain what is a method.
1. Explain how objects are passed as arguments.
1. Explain how to convert an object to a string.
# Inheritance
1. Explain how equality/sameness is in objects.
1. Explain what is inheritance.
1. Implement a super-sub class relationship.

# Answers

1. fruit = ['apple', 'banana', 'orange']
2. items_for_sale = [['Ford', 'Honda'], ['Star Wars', 'Independence Day']]
3. it would have to have 2 sub lists, or rather a sublist within another sublist. For example,
```python
exampleList = ["a", ["b", ["c", "d"]]]
print(exampleList[1][1][1])
```
would return d

4. Why is the first print line False but the second print line is True? *3 of 6 points*
```python
x = ["a","b"]
y = ["a","b"]
print (x is y)
print(x == y)
```
>Your Answer:
>The `is` checks if both the variables point to the same object whereas the `==` sign checks if the values for the two variables are the same. Since lists are always seperate objects, x `is not` y, however since they have the same variables within the lists, x `==` y.


5. True
6. [81, 17, 83, 81, 17, 83]
7. Suppose you have a list of items named cars that contains strings for “Ford”,”Honda”, and “Toyota”. Suppose you also have a list of items named planes that contains strings for “737” and “747”. Create a function that can take either list as an input parameter and print out each item in the list. Call the function for both lists. Your Answer:
```python
cars = ['Ford', 'Honda', 'Toyota']
planes = ['737', '747']


def functionx(list_name):
    for item in list_name:
        print(item)
        
functionx(cars)
functionx(planes)
```
8. Explain what a key-value pair is, and where you might use one in Python. *2 of 3 points* Your Answer:
>a key-value pair is used in dictionaries in Python. it defines that the first variable x is the key and y is the value associated with that key. It is written dictionary1 = {'a':0, 'b':1} where the letters 'a' and 'b' are the keys and the numbers 0, 1 are the values.
Key-value pairs are used in Python dictionaries. Each value of a dictionary is accessed by an unique “key”; so they are known as key-value pairs. Dictionaries are not sequences, so the order in which elements are added to the dictionary doesn’t matter.
Example: D = {'food': 'pudding', 'quantity': 4, 'color': 'pink'}
where in the dictionary `D`, food, quantity, and color are the keys and pudding, 4 and pink are the values.


9. 1 & 4
10. Explain the relationship between classes and objects. *1 of 3 points* Your Answer:

>A class is a blueprint, or set of instructions and information. An object is an actual thing that is built from the class. For example: A blueprint for a house design is like a class description. All the houses built from that blueprint are objects of that class.


11. What is inheritance and why is it a useful concept? *2 of 3 points* Your Answer:

> Classes can inherit from other classes. A class can inherit attributes and behaviour methods from another class or parent class. A class which inherits from a parent class is called a subclass


12. 
```python
def time_between_months(startingmonth, endingmonth):
    months = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
    difference = months[endingmonth] - months[startingmonth]
    return difference
print(time_between_months('May', 'November'))


