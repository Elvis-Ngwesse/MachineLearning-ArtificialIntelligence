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
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Is 17 prime?", is_prime(17))
print("Is 18 prime?", is_prime(18))
