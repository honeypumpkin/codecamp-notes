# Exam 2 Learning Objectives
## Conditionals
* *Describe what is a boolean.*
    * A data type with two values, True and False
    * Boolean expression: something that evaluates to True or False 
        * `2 > 4` - comparison (uses `<`, `>`, `==`, `!=`)
        * Boolean functions
        * Compound Boolean expressions (use `and`/`or`)
        
* *Describe what are logical operators.*

**

* *Describe the order of precedence with logical operators*

**

* *Write an if statement with an else clause.*
    * Smallest conditional expression
    ```python
    if condition: 
    elif condition: 
    else condition:
    ```   
    * Can put anything after the `if` as long as it evaluates to a boolean.

* *Write a (nested) if statement with an elif clause.*

**

* *Reduce a boolean function to a boolean expression.*

**

## More About Iteration
* *Write a for loop.*
    * `while` loop vs `for` loop: 
        * `for` loops: run a specific number of times (definate)
        * `while` loops: run until the given condition is false (indefinate) /**danger** watch out for infinate loops!! where the condition is always true./

* *Write a while loop.*

**

* *Explain what is an infinite loop.*
    * a while loop where the condition is always true

* *Explain how an image is stored digitally.*
    * Stored in pixel data
    * HOW TO PROCESS AN IMAGE
        1. Import/open image
        2. Get width/height
        3. Loop (nested `for` loops over W&H)
        4. Do something to each pixel
        5. Write/replace pixel

* *Explain how color is modeled on a computer.*
    * Every visible color* can be represented as an RGB value: (RGB) each is between [0-255] (*Actually only 255**2 colors...)

* *Write an program that processes an image.*

**

## Strings
* *Explain what is a collection data type and why a string is an example.*
    * Strings and Lists can be indexed so they are ORDERED collections (ie. the order determined by the index of each member)
    * A collection contains a set of values
    * A collection data type is a collection of values and a string is a good example because it can be broken down into its individual values.

* *Explain what is string concatenation and how to perform it in Python.*
    * `str3 = str1 + str2` this will generate 3 strings.
    * `str1 = str1 + str2` this will ALSO generate 3 strings

* *Explain what is string repetition and how to perform it in Python.*
    ```Python  
    str1 - "abc"
    str2 = str1 * 3 #is same as "abc" + "abc" + "abc"
    #returns 
    "abcabcabc"
    ```
* *Explain how to index into a string.*
    * Access a single character using bracket notation `[]`:
    ```python
    str2[5]
    #returns
    "c"
    ```
* *Describe some of the methods we can perform on strings.*
    * LOOK AT METHODS CHART
    
* *Explain how the len function works.*
    * The `len()` function gives us the number of characters in a string... ex...
    ```python
    len(str1) #YES - this is a function
    stri.len() #NO - this is a method
    ```
    * Need to remember the difference between method/function

* *Explain how the slice operator works.*
    * The slice operator `[n:m]` returns the part of the string from the `n`’th character to the `m`’th character, including the first but excluding the last.
    * If you omit the first index (before the colon), the slice starts at the beginning of the string. If you omit the second index, the slice goes to the end of the string.

* *Explain what are ordinal values in strings.*
    * Integer that corresponds to each character, and can be used to determine the ordinal value of each character. 
    ```python
    'b' < 'z'
    ord('b') < ord('z')
    ```
    * How does this apply to Lexicographical Order?
        * Capitals come before lowers. 
        * Corresponds with ASCII table.

* *Explain what it means for strings to be immutable.*
    * Strings are immutable, which means you cannot change an existing string. The best you can do is create a new string that is a variation on the original.
    * The solution here is to concatenate an edit onto a slice of your string. This operation has no effect on the original string.