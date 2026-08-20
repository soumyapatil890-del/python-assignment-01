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