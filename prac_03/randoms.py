import random
print(random.randint(5, 20))  # line 1

# What did you see on line 1?
# A random number between 5 and 20 including both 5 and 20

# What was the smallest number you could have seen, what was the largest?
# The smallest number was 5 and the largest was 20

print(random.randrange(3, 10, 2))  # line 2

#What did you see on line 2?
# A random number between 3 and 10. The step is 2

#What was the smallest number you could have seen, what was the largest?
# The smallest number was 3 and the largest was 9

#Could line 2 have produced a 4?
# line 3 couldn't have produced a 4 because the step is 2. All the outputs will be odd numbers

print(random.uniform(2.5, 5.5))  # line 3

#What did you see on line 3?
# A random floating point number between 2.5 and 5.5.

#What was the smallest number you could have seen, what was the largest?
# The smallest number was 2.6122 and the largest was 5.4352

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100)) 