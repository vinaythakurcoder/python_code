# Python Data Structures

Data structures are used to store, organize, and manage data efficiently.
Python provides built-in data structures that are easy to use and powerful.

---

## 1. List

### 1.1 What is a List?
- List is an ordered and mutable collection
- Allows duplicate values
- Defined using square brackets `[]`

### 1.2 Example

numbers = [1, 2, 3, 4]
names = ["Vinay", "Jhoshi", "Suresh"]

## Dictionary (dict)

**📌 Dictionaries are fast, flexible, and commonly used for structured data**

### Dictionary Important Methods

student = {
    "name": "Vinay",
    "age": 20,
    "course": "Python"
}


**1. keys() – returns all keys**

print(student.keys())

**2. values() – returns all values**

print(student.values())

**3. items() – returns key-value pairs**

print(student.items())

**4. get() – safely access value**

print(student.get("name"))

**5. update() – update or add values**

student.update({"age": 21, "city": "Delhi"})

**6. pop() – remove item by key**

student.pop("course")

**7. popitem() – remove last inserted item**

student.popitem()

**8. clear() – remove all items**

student.clear()