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
```python
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

- keys() – returns all keys
print(student.keys())

- values() – returns all values
print(student.values())

- items() – returns key-value pairs
print(student.items())

- get() – safely access value
print(student.get("name"))

- update() – update or add values
student.update({"age": 21, "city": "Delhi"})

- pop() – remove item by key
student.pop("course")

- popitem() – remove last inserted item
student.popitem()

- clear() – remove all items
student.clear()
