## Dictionary Important Methods – Python

student = {
    "name": "Vinay",
    "age": 20,
    "course": "Python"
}

# keys() – returns all keys
print(student.keys())

# values() – returns all values
print(student.values())

# items() – returns key-value pairs
print(student.items())

# get() – safely access value
print(student.get("name"))

# update() – update or add values
student.update({"age": 21, "city": "Delhi"})

# pop() – remove item by key
student.pop("course")

# popitem() – remove last inserted item
student.popitem()

# clear() – remove all items
student.clear()
