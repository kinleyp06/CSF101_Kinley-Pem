for i in range(1, 6):
    print(i)

count = 5
while count > 0:
    print(count)
    count -= 1

total = 0 
for num in range(1,11):
    total += num
print(f"The sum of numbers 1 to 10 is: {total}")

fruits = ["Apple", "Banana", "Cherry"]
for fruits in fruits:
    print(fruits)

for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} * {j} = {i*j}")
    print() 