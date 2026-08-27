# Python Assignments

This repository contains a collection of Python programming assignments
organized topic-wise according to the assignment tracker.

## Repository Structure

```text
Python_Assignments
│
├── 01_Interpreted_and_Dynamic_Nature
│   ├── Assignment_01
│   │   ├── assignment_1_1_dynamic_typing.py
│   │   ├── assignment_1_2_interpreted_behavior.py
│   │   └── assignment_1_3_strong_typing.py
│   │
│   ├── Assignment_02
│   │   └── assignment_2_1_identity_vs_value.py
│   │
│   └── Assignment_03
│       ├── assignment_3_1_legb.py
│       └── assignment_3_2_global_nonlocal.py
│
├── 02_Variables
│   ├── assignment1.py
│   ├── assignment2.py
│   └── assignment3.py
│
├── 03_Core_Data_Types
│   ├── assignment1.py
│   └── assignment2.py
│
├── 04_Working_With_Data
│   ├── assignment1.py
│   ├── assignment2.py
│   └── assignment3.py
│
├── 05_Control_Statements
│   ├── assignment1.py
│   ├── assignment2.py
│   └── assignment3.py
│
└── README.md
```

# 01 - Interpreted & Dynamic Nature

This topic demonstrates important characteristics of Python including
dynamic typing, interpreted behavior, strong typing, object identity,
value comparison, scope resolution, and namespaces.

## Assignment 01 - Interpreted & Dynamic Nature

### Assignment 1.1 - Dynamic Typing

The variable `data` is first assigned an integer and then reassigned a list.

The `type()` function is used to verify the type after each assignment.

### Concepts Demonstrated

- Dynamic typing
- `type()` function
- Runtime type identification

### Assignment 1.2 - Interpreted Behavior

The program successfully executes the first two statements and then
deliberately references an undefined variable.

This produces a `NameError`.

### Concepts Demonstrated

- Runtime execution
- `NameError`
- Program execution stopping after an error

### Assignment 1.3 - Strongly Typed Behavior

The original program attempts to concatenate an integer with strings,
which produces a `TypeError`.

The problem is fixed using:

1. Explicit type casting with `str()`
2. An f-string

### Concepts Demonstrated

- Strong typing
- `TypeError`
- Explicit type casting
- String formatting

## Assignment 02 - Identity vs. Value

This assignment demonstrates the difference between value equality
and object identity in Python.

The program analyzes mutable lists using the `==` and `is` operators,
prints object identities using `id()`, demonstrates shared references
and mutability, and explores small integer caching using 256 and 257.

### Concepts Demonstrated

- Value comparison using `==`
- Object identity using `is`
- `id()` function
- Mutable objects
- Shared references
- Small integer caching

### Key Observations

- `list1 == list2` is `True` because both lists contain the same values.
- `list1 is list2` is `False` because they are different list objects.
- `list1 is list3` is `True` because `list3` refers to the same object as `list1`.
- Modifying `list1` also changes `list3` because both reference the same mutable list.
- Small integer caching can affect identity comparisons such as `a is b`.
- `==` should be used for value comparison, while `is` should be used for object identity.

## Assignment 03 - Scope and Namespaces

This assignment demonstrates Python's scope resolution rules and the
use of the `global` and `nonlocal` keywords.

### Task 3.1 - LEGB Lookup Order

The program demonstrates the LEGB rule:

- Local
- Enclosing
- Global
- Built-in

The value of `x` is traced through local, enclosing, and global scopes
by changing the definitions and observing which value Python resolves.

### Task 3.2 - Global and Nonlocal

The program demonstrates how `global` can modify a variable defined in
the global scope and how `nonlocal` can modify a variable from an
enclosing function scope.

### Concepts Demonstrated

- LEGB scope resolution
- Local scope
- Enclosing scope
- Global scope
- `global` keyword
- `nonlocal` keyword
- Nested functions

# 02 - Variables

This section contains Python exercises focused on variables,
variable naming, string formatting, and basic calculations.

## Assignment 01 - Student ID Card Generator

Create variables to store:

- Student Name
- Roll Number
- Branch
- Semester
- College Name

The program prints the student details in a neatly formatted ID card.

**Bonus:** Creates an `email_id` using the student's name and roll number.

### Concepts Demonstrated

- Variable creation
- String values
- Formatted output
- String methods
- F-strings

## Assignment 02 - Variable Naming Inspector

Analyze the following variable names:

- `EmployeeName`
- `employee_name`
- `employee-name`
- `employeeName`
- `Employee_Name`
- `employee1`
- `1employee`

The program identifies valid and invalid names, rewrites invalid names,
and mentions which names follow Python best practices.

### Concepts Demonstrated

- Variable naming rules
- Valid and invalid identifiers
- `snake_case`
- Naming conventions
- Python best practices

## Assignment 03 - Grocery Bill

Store:

- Shop Name
- Item 1 Price
- Item 2 Price
- Item 3 Price

Calculate:

- Total
- GST (18%)
- Final Amount

The program then prints a formatted grocery bill.

### Concepts Demonstrated

- Variables
- Arithmetic operations
- Percentage calculation
- F-strings
- Basic output formatting

# 03 - Core Data Types

This section contains Python exercises focused on selecting and
working with appropriate built-in data types for real-world data.

## Assignment 01 - Hospital Patient Record

Stores:

- Patient Name
- Age
- Weight
- Is Insured

The program prints each value along with its datatype and explains
why the selected datatype is appropriate.

### Concepts Demonstrated

- `str`
- `int`
- `float`
- `bool`
- `type()`
- Datatype selection

## Assignment 02 - Online Exam Result

Stores:

- Student Name
- Marks Obtained
- Percentage
- Passed (`True` / `False`)

The program prints a result summary and, when the student fails,
calculates the additional marks needed to reach the passing mark of 35.

### Concepts Demonstrated

- `str`
- `int`
- Boolean values
- Boolean expressions
- `True` / `False`
- Basic calculations

# 04 - Working With Data

This section contains Python exercises focused on performing
calculations and manipulating data using variables and basic
built-in operations.

## Assignment 01 - Electricity Bill

Stores:

- Previous Reading
- Current Reading
- Cost per Unit

Calculates:

- Units Consumed
- Total Bill

The program then prints the electricity bill.

### Concepts Demonstrated

- Arithmetic calculations
- Subtraction
- Multiplication
- Variables
- Formatted output

## Assignment 02 - Product Discount

Stores:

- Product Price
- Discount Percentage

Calculates:

- Discount Amount
- Final Price

The final price is rounded to two decimal places.

### Concepts Demonstrated

- Percentage calculations
- Arithmetic operations
- `round()`
- Variables
- Formatted output

## Assignment 03 - Company Email Generator

Stores:

- First Name
- Last Name
- Company Name

Generates a company email in the required format.

The program then displays:

- Original Name
- Uppercase Email
- Email Length

### Concepts Demonstrated

- String concatenation
- `lower()`
- `upper()`
- `len()`
- String formatting

# 05 - Control Statements

This section contains Python exercises focused on conditional
statements, loops, and controlling program flow.

## Assignment 01 - ATM Withdrawal

Stores:

- Account Balance
- Withdrawal Amount

The program checks whether the balance is sufficient.

If the balance is sufficient:

- Displays `Transaction Successful`
- Prints the remaining balance

Otherwise:

- Displays `Insufficient Balance`

### Concepts Demonstrated

- `if` statements
- `else` statements
- Comparison operators
- Conditional logic
- Arithmetic operations

## Assignment 02 - Login Attempts

Allows a maximum of three login attempts.

The correct password is:

`admin123`

The program displays:

- `Login Successful`
- `Try Again`
- `Account Locked`

depending on the login result.

A `while` loop is used to control the attempts.

### Concepts Demonstrated

- `while` loops
- `if` statements
- `else` statements
- `break`
- Comparison operators
- Counters
- Conditional logic

## Assignment 03 - Even Numbers Printer

Uses a `for` loop to print all even numbers from 1 to 50.

The program also counts and displays the total number of even
numbers printed.

### Concepts Demonstrated

- `for` loops
- `range()`
- Modulo operator `%`
- Counters
- Conditional logic

# Topics Covered

The repository currently covers:

1. Interpreted & Dynamic Nature
2. Variables
3. Core Data Types
4. Working With Data
5. Control Statements