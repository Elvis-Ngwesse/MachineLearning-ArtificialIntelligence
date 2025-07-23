# Python Basics: variables, control flow, functions

# Variables and types
x = 10
y = 3.14
name = "Alice"
is_student = True

print("Type examples:")
print(type(x), type(y), type(name), type(is_student))

# Control flow
if x > 5:
    print(f"{x} is greater than 5")
else:
    print(f"{x} is 5 or less")

# For loop
print("For loop:")
for i in range(5):
    print(f"Loop {i}")

# While loop
print("While loop:")
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1

# Function
def greet(name):
    return f"Hello, {name}!"

print(greet("Bob"))
print(greet("Alice"))

# Prime checker
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):  # check from 2 up to n-1
        if n % i == 0:
            return False
    return True

"""
🔹 for i in range(2, n):
    This means:
    "Start from 2, and go up to n-1."
    Example: if n = 7, it checks: 2, 3, 4, 5, 6
You're looping over all possible divisors of n (except 1 and n itself).

 if n % i == 0:

    This means:
    "If n divided by i has no remainder, then i divides n exactly."

    The % operator is called modulo — it gives the remainder.
"""
# Run this only if the script is executed directly
if __name__ == "__main__":
    print("Is 17 prime?", is_prime(17))  # Or any number you want