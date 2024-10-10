#!/usr/bin/env pyhton3

number_1 = int(input("Enter the first number:\n"))
number_2 = int(input("Enter the second number:\n"))

result = number_1 * number_2

print(f"{number_1} x {number_2} = {result}")

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")