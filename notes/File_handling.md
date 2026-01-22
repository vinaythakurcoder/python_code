## Dictionary Important Methods – Python

student = {
    "name": "Vinay",
    "age": 20,
    "course": "Python"
}

### 1. keys() – returns all keys

print(student.keys())

### 2. values() – returns all values

print(student.values())

### 3. items() – returns key-value pairs

print(student.items())

### 4. get() – safely access value

print(student.get("name"))

### 5. update() – update or add values

student.update({"age": 21, "city": "Delhi"})

### 6. pop() – remove item by key

student.pop("course")

### 7. popitem() – remove last inserted item

student.popitem()

### 8. clear() – remove all items

student.clear()
