#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "fibonacci https://www.geeksforgeeks.org/python-program-for-program-for-fibonacci-numbers-2/"


def add(x, y):
    return x+y
print(add(2,3))


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    multiplied = 0
    for i in range(0, x):
        multiplied = add(multiplied, y)
    return multiplied
print(multiply(2,3))


def power(x, n):
    power = 1
    for i in range(0, n):
        power = multiply(power, x)
    return power
print(power(2, 3))


def factorial(x):
    factorial = 1
    if x < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif x == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, x + 1):
            factorial = factorial*i
    return (factorial)


print(factorial(7))


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    if n<0:
        print("Incorrect input") 
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(9))


if __name__ == '__main__':
    # your code to call functions above
    pass
