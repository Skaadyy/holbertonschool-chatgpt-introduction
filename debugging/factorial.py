#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            number = int(sys.argv[1])
            if number < 0:
                sys.exit(1)
            print(factorial(number))
        except Exception:
            sys.exit(1)
    else:
        sys.exit(1)
