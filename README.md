# PYTHON

# Assignment 01: Python Basics

A simple script covering two fundamental tasks: a basic calculator and a personalized greeter.

## What It Does
The script performs two distinct tasks:
1.  **Mathematical Calculator:** Accepts two floating-point numbers and performs addition, subtraction, multiplication, and division.

### Task 1: Math Operations
* **Input:** Takes two numbers (floats) from the user.
* **Process:** Calculates sum, difference, product, and quotient.
* **Output:** Prints the results to the console.

2.  **Personalized Greeting:** Accepts a first and last name to generate a formatted welcome message.

### Task 2: String Formatting
* **Input:** Takes first name and last name strings.
* **Process:** Concatenates strings to form a full name.
* **Output:** Displays a combined greeting string.


## How to Run
Make sure you have Python installed, navigte to the folder, and run:

```bash
python Assignment01.py


# Assignment 02: Conditions & Loops

A script demonstrating control flow using `if-else` statements and `for` loops.

## What It Does
1.  **Even/Odd Checker:** Asks for a number and tells you if it is even or odd.
### Task 1: Even/Odd Checker
* **Input:** Takes one integer from the user.
* **Process:** Uses the modulo operator (`%`) to check divisibility by 2.
* **Output:** Prints a message stating if the number is Even or Odd.


2.  **Sum Calculator:** Calculates and displays the sum of all numbers from 1 to 50.
### Task 2: Loop Summation
* **Input:** None (Automated process).
* **Process:** Iterates through numbers 1 to 50 using a `for` loop and maintains a running total.
* **Output:** Displays the calculated sum of the range.

## How to Run
Run the script in your terminal:

```bash
python Assignment02.py


# Assignment 03: Functions & Modules

A single Python script demonstrating the use of user-defined functions, recursion, and Python's built-in `math` module.

## What It Does

1.  **Factorial Calculator:** Asks for a number and calculates its factorial using a recursive function.

### Task 1: Factorial Using Recursion
* **Input:** Takes an integer from the user.
* **Process:** Defines a recursive function `factorial(n)` that multiplies the number by the factorial of `n-1` until it reaches the base case (0 or 1).
* **Output:** Returns and prints the calculated factorial.



2.  **Math Module Operations:** Performs advanced mathematical calculations on a user-provided number.

### Task 2: Math Module Operations
* **Input:** Takes a number (integer or float) from the user.
* **Process:** Imports the `math` module to calculate:
    * Square Root (`sqrt`)
    * Natural Logarithm (`log` base *e*)
    * Sine (`sin` in radians)
* **Output:** Displays the results for all three operations.


## How to Run
Run the script in your terminal:

```bash
python Assignment03.py


# Assignment 04: File Handling & Exception Handling

A Python script demonstrating file I/O operations (Read, Write, Append) and graceful error handling using `try-except` blocks.

## What It Does

1.  **Safe File Reader:** Attempts to read a file and print its contents, catching errors if the file is missing.

### Task 1: Read a File and Handle Errors
* **Input:** Targeted filename (e.g., `sample.txt`).
* **Process:**
    * Uses a `try-except` block to catch `FileNotFoundError`.
    * Reads the file line-by-line using `readlines()`.
    * Enumerates and prints each line.
* **Output:** Displays file content with line numbers or a friendly error message if the file is missing.


2.  **File Writer & Appender:** Accepts user input to create a file, appends data to it, and displays the final result.

### Task 2: Write and Append Data
* **Input:** Takes text input from the user.
* **Process:**
    1.  **Write Mode (`w`):** Creates `output.txt` and writes the user's input plus a default line.
    2.  **Append Mode (`a`):** Re-opens the file to append a final line without erasing existing data.
    3.  **Read Mode (`r`):** Reads the file back to verify all data was saved.
* **Output:** Prints the final consolidated content of `output.txt`.

## How to Run
Run the script in your terminal:

```bash
python Assignment04.py


# Assignment 05: Data Structures

A Python script demonstrating the manipulation of core data structures: Dictionaries and Lists.

## What It Does

1.  **Marks Lookup System:** Uses a dictionary to store and retrieve student grades based on names.
### Task 1: Dictionary of Student Marks
* **Input:** Takes a student's name as input.
* **Process:**
    * Defines a dictionary `student_marks` mapping names (keys) to scores (values).
    * Checks if the input name exists in the dictionary.
* **Output:** Displays the student's marks or an error message if the name is not found.


2.  **List Slicing & Reversing:** manipulates a numeric list to extract and reverse specific segments.


### Task 2: List Slicing
* **Input:** None (Uses a predefined list of numbers 1–10).
* **Process:**
    * **Slicing:** Extracts the first five elements (`[:5]`).
    * **Reversing:** Reverses the extracted sub-list using step slicing (`[::-1]`).
* **Output:** Prints both the extracted sub-list and the reversed version.

## How to Run
Run the script in your terminal:

```bash
python Assignment05.py