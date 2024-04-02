import random

with open("task1.txt", "w") as file:
    for _ in range(10000):
        file.write(str(random.choice(range(100))) + "\n")

with open("task1.txt", "r") as file:
    numbers = list(map(int, file))

print(numbers)
print(sum(numbers))
