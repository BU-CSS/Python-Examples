# Session 1
These scripts provide examples of the concepts explored during the first Python programming session.

## Hello World
* `01_basic.py` is the simplest form of a Python hello world script.
* `02_var_example.py` expands on the first example to include a variable.

## Input and Conditions
* `01_read_input.py` demonstrates how to read user input from the terminal and then displays it back to the user.
* `02_conditions.py` performs different operations based on user input by evaluating it against conditional statements.

## Loops
* `01_while_loop.py` improves the conditions example script by incorporating a while loop so the program can continue to take input commands.
* `02_for_loop.py` demonstrates a for loop by counting to a number specified by the user. This example also introduces `try...except` for catching non-int values.
* `03_iterator.py` iterates over each item in a list and prints each value.
* `04_iterator_with_import.py` is a more efficient implementation of the previous example that utilises the `string` module to create the list.

## Functions
* `01_function.py` shows the use of a simple function that prints the provided value.

## Calculator
This was the first challenge of session 1 where you were asked to build a simple calculator. The script included here is how we would complete this challenge, while there are many other ways to approach the task we wanted to enforce the topics covered in the session.

The `calc.py` script takes three inputs from the user; 2 numbers and an operation. The operation can be `add`, `sub`, `mult`, `div`, `+`, `-`, `/`, `*` or `exit`. The conditional statements us the `or` operator so that, for example the code
```python
print(add(first_number, second_number))
```
is run if the user enters either `and` or `+` as the operation input.

Different functions are called based on the operation the user inputs. The program is contained within a `while` loop so that multiple calculations can be performed consecutively.

## Chat Application
*Awaiting final challenge plans.*
