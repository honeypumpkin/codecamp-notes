# PROBLEMS WITH DICTIONARIES

1. nothing to enforce use of correct keys
1. no way to 'bind' behaviors to data they should be used for
```python
compute_gpa('Chris')    ## problem here!! can't use a string to compute a function.
```
# FIX BY...

1. create a class
    * a class is a template for creating objects.
        * classes have both data (variables) and behaviors (functions)

        ```python
        class Student:
            def __init__(self, first_name, last_name, student_id):
                self.first_name = first_name
                self.last_name = last_name
                self.student_id = student_id

        chris = Student('Chris', 'Bay', 123456)

        print(chris.first_name)
        print(chris.last_name)
        print(chris.student_id)
        ```
## Objects:

* An object is something created from a specific class
* An object is an instance of a class

## `__init__`

* `__init__` is our class' initializer or constructor

```python
class Student:
    # data
    def __init__(self,) 
chris = Student('Chris', 'Bay', 123456)
````

* `__init__` initializes or runs the class of Student.

## `self` 
* is function specific. it refers to the self in the specific function running.
```python 
    self.first_name = first_name
    chris = Student('Chris', 'Bay', 123456)
```

## CLASSES
* classes have attributes:
    * variables
    * member variables (belong to specific types of objects)
    * functions
    * member functions (belong to a spec...)
    * methods ***This is what we call it***
* To use attributes, we use dot-notation




