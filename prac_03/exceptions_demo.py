"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"""
Ans:

1. When will a ValueError occur?
A ValueError occur when the numerator or denominator is not integer.

2. When will a ZeroDivisionError occur?
A ZeroDivisionError occur when the denominator is zero.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, we can change the code to avoid the possibility of a ValueError by adding error checking condition before the division.
"""