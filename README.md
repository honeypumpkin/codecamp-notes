# CodeCamp Notes

**Lesson notes for CodeCamp**

## Lesson 3
*Debugging*

### There are 3 types of errors that can occur:
1. syntax errors
2. runtime errors
3. semantic errors

#### Syntax Errors
Syntax refers to the structure of a program and the rules about that structure.
ie. forgetting a semicolon or closing a parens

*example* 
```python
print("Syntax errors are from missing bits)
```

#### Runtime Errors
These are also called exceptions as they indicate something exceptional (bad) has happened.

*example*
```python
print(6 / 0)
```

#### Semantic Errors
If there is a semantic error in your program, it will run successfully in the sense that the computer will not generate any error messages. However, your program will not do the right thing. It will do something else. Specifically, it will do what you told it to do.

*example*
```python
percent = 15
print("15% of 100 is " , percent)
```
we forgot to divide by 100 before having the percentage amount

### Avoid having to debug
1. Start small
Run your code as you are writing it - every 2 lines will help you isolate bugs as they are introduced.

2. Keep it working 
Once you have a working program, add small bits at a time to keep it working. If you introduce a bug you are able to isolate where it was added.

__**"Get something working and keep it working"**__
-Said by someone really important I bet

*example*
``` python
current_time = input("what is the current time (in hours)?")
wait_time = input("How many hours do you want to wait")

print(current_time)
print(wait_time)
```
This works great - let's add on...

``` python
current_time = input("What is the current time (in hours 0 - 23)?")
wait_time = input("How many hours do you want to wait")

print(current_time)
print(wait_time)

final_time = current_time + wait_time
print(final_time)
```
Uh oh. So now we are missing a way to make the numbers add correctly. Converting to an integer will help.

``` python
current_time_str = input("What is the current time (in hours 0-23)?")
wait_time_str = input("How many hours do you want to wait")

current_time_int = int(current_time_str)
wait_time_int = int(wait_time_str)

final_time_int = current_time_int + wait_time_int
print(final_time_int)
```
Great! But testing out 13 gives the wrong answer. Need to add a modulo to account for the 0-23 hours...

``` python
current_time_str = input("What is the current time (in hours 0-23)?")
wait_time_str = input("How many hours do you want to wait")

current_time_int = int(current_time_str)
wait_time_int = int(wait_time_str)

final_time_int = current_time_int + wait_time_int

final_answer = final_time_int % 24

print("The time after waiting is: ", final_answer)
```

Perfect! Testing after each stage saved us time.

### Tips for Debugging
1. Everyone is a suspect (except Python!). Don't blame Python. It is more then likely you :(
2. Find clues. There are 2 important clues to look for when debugging:
    * Error messages
    * Print statements

Four major error types:
1. ParseError
2. TypeError
3. NameError
4. ValueError

#### ParseError
A ParseError happens when you make an error of the syntax of your code. All ParseErrors are syntax errors, but not all syntax errors are ParseErrors.
Usually ParseErrors can be traced back to missing punctuation characters such as commas, quotes, and parentheses.

Many times, your code editor will tell you where the error is: 
```
ParseError: bad input on line 5
```
However, this isn't always exactly right. Start at the line mentioned and work your way back.  

##### Finding clues
If you have trouble spotting the error a good place to start is to comment out the line mentioned in the error message.

#### TypeError
TypeErrors occur when you you try to combine two objects that are not compatible. For example you try to add together an integer and a string. Usually type errors can be isolated to lines that are using mathematical operators, and usually the line number given by the error message is an accurate indication of the line.

#### NameError
Name errors almost always mean that you have used a variable before it has a value. Often NameErrors are simply caused by typos in your code. They can be hard to spot if you don’t have a good eye for catching spelling mistakes. Other times you may simply mis-remember the name of a variable or even a function you want to call. 

Can you spot the NameError?
``` python
str_time = input("What time is it now?")
str_wait_time = input("What is the number of hours to wait?")
time = int(str_time)
wai_time = int(str_wait_time)

time_when_alarm_go_off = time + wait_time
print(time_when_alarm_go_off)
```
Line 4 misspelled wait_time... 

##### Finding clues
An easy way is to use the cmd+F and find the different variable names. Often you will be looking at a line and if the variable doesn't hilight it has been misspelled.

#### ValueError
Value errors occur when you pass a parameter to a function and the function is expecting a certain type, but you pass it a different type. We can illustrate that with this particular program in two different ways.