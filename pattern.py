

for i in range(1, 6):
    print("*" * i)


for i in range(1,10):
    for j in range (1,i+1):
        print("*",end="")
    print()

for i in range(1, 6):
    print(" " * (5 - i) + " *" * i)


for i in range(1, 6):
    print(" " * (5 - i) + "*" * (2 * i - 1))


for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()


for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end="")
    print()


 
for i in range(65, 75):
    for j in range(65, i + 1):
        print(chr(i), end="")
    print()

for i in range(1, 6):
    for j in range(65, 65 + i):
        print(chr(j), end="")
    print()

for i in range(2000, 3201):
    if i % 5 == 0 and i % 7 != 0:
        print(i)
