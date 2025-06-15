numbers_input = input("Enter 5 numbers separated by spaces: ")
numbers = [int(num) for num in numbers_input.split()]

print(f"The first number is: {numbers[0]}")
print(f"The last number is: {numbers[-1]}")
print(f"The smallest number is: {min(numbers)}")
print(f"The largest number is: {max(numbers)}")
print(f"The average number is: {sum(numbers)/len(numbers)}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username_input = input("Enter username: ")
if username_input in usernames:
    print("Access granted")
else:
    print("Access denied")