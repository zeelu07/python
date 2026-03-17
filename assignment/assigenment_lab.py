# 1. Hello World Program
print("Hello World")


# 2. Simple Client-Server Simulation (NO requests → error-free)

import urllib.request

try:
    response = urllib.request.urlopen("https://www.google.com")
    print("Status Code:", response.status)
except:
    print("Request failed")

# 4. Internet Speed Type
connection = input("Enter connection (broadband/fiber): ")

if connection == "fiber":
    print("High speed and reliable")
elif connection == "broadband":
    print("Moderate speed")
else:
    print("Unknown connection")


# 5. Simple Encryption
message = "Hello"
encrypted = ""

for char in message:
    encrypted += chr(ord(char) + 1)

print("Encrypted message:", encrypted)


# 6. Software Classification
software = {
    "Windows": "System",
    "Chrome": "Application",
    "Antivirus": "Utility"
}

for key, value in software.items():
    print(key, "->", value)


# 7. SDLC Steps
steps = ["Requirement", "Design", "Development", "Testing", "Deployment", "Maintenance"]

for step in steps:
    print(step)


# 8. Calculator
a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)

if b != 0:
    print("Division:", a / b)
else:
    print("Cannot divide by zero")


# 9. Login System
username = "admin"
password = "1234"

u = input("Enter username: ")
p = input("Enter password: ")

if u == username and p == password:
    print("Login Successful")
else:
    print("Invalid Credentials")


# 10. Registration Flow
print("Start")

name = input("Enter Name: ")

if name != "":
    print("Data Valid")
    print("Submitted Successfully")
else:
    print("Invalid Data")

print("End")


