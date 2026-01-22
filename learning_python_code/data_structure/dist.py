
## Dictionary (dict)

# 1. Student information
student = {
    "name": "Vinay",
    "age": 20,
    "course": "Python"
}

# 2. Mobile details
mobile = {
    "brand": "Samsung",
    "price": 15000,
    "in_stock": True
}

# 3. Employee data
employee = {
    "id": 101,
    "name": "Amit",
    "salary": 45000
}

# 4. Accessing dictionary values
print(student["name"])
print(mobile["price"])

# 5. Updating dictionary
student["age"] = 21

# 6. Adding new key-value
student["city"] = "Delhi"

# 7. Dictionary with mixed data types
data = {
    1: "One",
    2: 200,
    3.5: "Three Point Five"
}

# 8. Nested dictionary
school = {
    "student1": {"name": "Rahul", "marks": 85},
    "student2": {"name": "Neha", "marks": 90}
}

data = {"a": 1, "b": 2}
print(data.keys())



# 📘 Dictionary – All Functions in One Code

data = {
    "name": "Vinay",
    "age": 20,
    "course": "Python"
}

print("Original dict:", data)

# keys()
print("Keys:", data.keys())

# values()
print("Values:", data.values())

# items()
print("Items:", data.items())

# get()
print("Get name:", data.get("name"))
print("Get city (safe):", data.get("city"))

# update()
data.update({"age": 21, "city": "Delhi"})
print("After update:", data)

# pop()
data.pop("course")
print("After pop:", data)

# popitem()
data.popitem()
print("After popitem:", data)

# copy()
new_data = data.copy()
print("Copied dict:", new_data)

# len()
print("Length:", len(data))

# in keyword
print("Is 'name' in data?", "name" in data)

# clear()
data.clear()
print("After clear:", data)

# Sort dictionary by key
sample = {"c": 3, "a": 1, "b": 2}
sorted_dict = dict(sorted(sample.items()))
print("Sorted by key:", sorted_dict)
