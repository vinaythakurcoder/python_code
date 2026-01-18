
f = open("functions.py", "r")
line1= f.readline()
line2= f.readline()
line3= f.readline()
line4= f.readline()
print(line1)
print(line2)
print(line3)
print(line4)

print("ThakurSabji......")


with open("functions.py", "r")as f:
    print(f.read())

import os
print(os.getcwd())


