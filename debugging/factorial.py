#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./factorial.py <number>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        print(factorial(number))
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)
