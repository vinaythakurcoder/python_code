# Reading a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Writing to a file
with open('example.txt', 'w') as file:
    file.write('Hello, World!')

# Appending to a file
with open('example.txt', 'a') as file:
    file.write('\nNew line')

# Reading line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())

# Reading all lines into a list
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print(lines)