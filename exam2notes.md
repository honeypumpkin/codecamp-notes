# Exam 2 Learning Objectives
## Conditionals
* *Describe what is a boolean.*
    * A data type with two values, True and False
    * Boolean expression: something that evaluates to True or False 
        * `2 > 4` - comparison (uses `<`, `>`, `==`, `!=`)
        * Boolean functions
        * Compound Boolean expressions (use `and`/`or`)
        
* *Describe what are logical operators.*
    * Not
    * And
    * Or

* *Describe the order of precedence with logical operators*
    * Not
    * And 
    * Or

* *Write an if statement with an else clause.*
    * Smallest conditional expression
    ```python
    if condition: 
    elif condition: 
    else condition:
    ```   
    * Can put anything after the `if` as long as it evaluates to a boolean.

* *Write a (nested) if statement with an elif clause.*
    ```python
    if expression1:
        statement(s)
    elif expression2:
        statement(s)
    elif expression3:
        statement(s)
    else:
        statement(s)
    ```
* *Reduce a boolean function to a boolean expression.*
    ```python
    def isDivisible(x, y):
    return x % y == 0
    ```

## More About Iteration
* *Write a for loop.*
    * `while` loop vs `for` loop: 
        * `for` loops: run a specific number of times (definate)
        * `while` loops: run until the given condition is false (indefinate) /**danger** watch out for infinate loops!! where the condition is always true./

* *Write a while loop.*
    ````python
    count = 0
    while (count < 9):
        print 'The count is:', count
        count = count + 1

    print "Good bye!"   
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

# THE EXAM
1. What is the output of this statement?

j = 24
print(j % 2)


0

2. How can you rewrite the following code into something with fewer lines of code?

a = 14
if a > 20:
     print(True)
else:
     print(False)

Your Answer:
a = 14

print(a > 20)

3. What is the output of this statement?

x = 16
print(x > 15 and 2 == 3)


False

4. What is the output of this statement?

x = 4
y = 6

print((x > 2 and 6 > 4) or (y < 2))


True

5. Write a few lines of code that assign a value to x and then test if x is between 5 and 15, printing True if that’s the case, and False if it is not.

Your Answer:
x = 14

print(x > 5 and x < 15)

6. Declare a variable named animal that receives user input for a kind of animal. Then write an If statement wherein if animal equals "lion", print "roar", otherwise print "this is not a lion."

Your Answer:
animal = input("What kind of animal would you like?")

if animal == "lion":

    print("roar")

else:

    print("this is not a lion")

7. What is the output of this statement?

if 7 * 2 > 4:
     print("TRUE")
else:
     print("FALSE")
print("TRUE")

Your Answer:
"TRUE"

"TRUE"

8. Write nested if statements that reflect the following:

Variable: temperature

Is Warm

Is Cold


Variable: rain

Is Rainy

Print Play in the Rain

Print Stay Indoors

Is Dry

Print Go Swimming

Print Layer Up

Your Answer:
def weather(x, y):

if x == "Rainy":

if y == "Warm":

print("Play in the Rain")

else:

print("Stay Indoors")

elif x == "Dry":

if y == "Warm":

print("Go Swimming")

else:

print("Layer Up")

 

print(weather(Dry, Warm))

9. Write if and else-if statements that reflect the following:

Variable: animal

Print

lion

roar

sheep

baaa

cat

meow

none of the above (else)

unknown

Your Answer:
animal = x

if animal == "lion":

    print("roar")

elif animal == "sheep":

    print("baa")

elif animal == "cat":

    print("meow")

else:

    print("unknown")

10. Using the following starter code, implement a while loop that adds 1 gallon of gas to the car’s tank as long as the gas level is below the capacity of the tank.  At the end of the loop, the car should have a full tank of gas. **WRONG**

car_fuel_capacity = 13
gallons_pumped = 0
gas_in_the_car = 4

Your Answer:
car_fuel_capacity = 13
gallons_pumped = 0
gas_in_the_car = 4

while gas_in_the_car =< car_fuel_capacity:

    gas_in_car = gas_in_car + 1 

return gas_in_car

gallons_pumped = gas_in_car - 4

print("You have pumped ", gallons_pumped, " to fill your tank to ", gas_in_the_car, ", which is equal to your capacity of ", car_fuel_capacity, ".")

11. Under what circumstances might you use a while loop instead of a for loop? **WRONG**

Your Answer:
When you need to iterate the loop for longer then just the string length (ie when you need the loop to reach a certain value), or when you need input from user to command loop to stop.

12. Given the variable below, print out the first and last initials of the name: **WRONG**

username = “John Smith”

Your Answer:
username = “John Smith”

print[0, 5]

13. Strings are immutable. Explain what this concept means.

Your Answer:
This means they cannot be changed at the base-level. You can create new strings with substitutions which look like the string has changed, but the original string is still there, just no longer being pointed to.
