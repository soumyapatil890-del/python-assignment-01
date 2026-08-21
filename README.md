# Python Assignment 02 - Identity vs. Value

## Overview

This assignment demonstrates the difference between value equality
and object identity in Python.

## Assignment 2.1

The program analyzes mutable lists using the `==` and `is` operators,
prints object identities using `id()`, demonstrates shared references
and mutability, and explores small integer caching using 256 and 257.

## Concepts Demonstrated

- Value comparison using `==`
- Object identity using `is`
- `id()` function
- Mutable objects
- Shared references
- Small integer caching

## Key Observations

- `list1 == list2` is `True` because both lists contain the same values.
- `list1 is list2` is `False` because they are different list objects.
- `list1 is list3` is `True` because `list3` refers to the same object as `list1`.
- Modifying `list1` also changes `list3` because both reference the same mutable list.
- Small integer caching can affect identity comparisons such as `a is b`.
- `==` should be used for value comparison, while `is` should be used for object identity.