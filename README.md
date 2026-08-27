# Python Assignment 01 - Interpreted & Dynamic Nature

## Overview

This assignment demonstrates three important characteristics of Python:

1. Dynamic Typing
2. Interpreted Behavior
3. Strong Typing

## Assignment 1.1 - Dynamic Typing

The variable `data` is first assigned an integer and then reassigned a list.

The `type()` function is used to verify the type after each assignment.

### Concepts Demonstrated

- Dynamic typing
- `type()` function
- Runtime type identification

## Assignment 1.2 - Interpreted Behavior

The program successfully executes the first two statements and then deliberately references an undefined variable.

This produces a `NameError`.

### Concepts Demonstrated

- Runtime execution
- `NameError`
- Program execution stopping after an error

## Assignment 1.3 - Strongly Typed Behavior

The original program attempts to concatenate an integer with strings, which produces a `TypeError`.

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

### Assignment 2.1

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


## Variables

This section contains Python exercises focused on variables,
variable naming, string formatting, and basic calculations.

### Assignment 01 - Student ID Card Generator

Create variables to store:

- Student Name
- Roll Number
- Branch
- Semester
- College Name

The program prints the student details in a neatly formatted ID card.

**Bonus:** Creates an `email_id` using the student's name and roll number.

### Assignment 02 - Variable Naming Inspector

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

### Assignment 03 - Grocery Bill

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
- Variable naming rules
- `snake_case`
- String methods
- F-strings
- Arithmetic operations
- Basic output formatting