name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read()
in_file.close()
print(f"Hi {name}!")

with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    result = first_number + second_number
print(f"The result of adding the first two number is {result}")

total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += int(line)
    print(f"Total of numbers is {total}")
