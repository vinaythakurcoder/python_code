list1 = ["Mumbai", "Chennai", "Bangalore", "Hyderabad", "Delhi"]
list2 = ["Suraj", "Rahul", "Sovit", "vinay", "kumar", "Ankit"]

def len_list(list):
    print(list)

len_list(list1)
len_list(list2)

def factorial(n):
    result = 1
    while n > 1:
        result = result * n
        n = n - 1
    return result

print(factorial(5))

def largest_number(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest
print(largest_number([10, 25, 5, 78, 99, 34]))

# write a function to print squar and cube the given number.

def number(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
number(10000)

# write a function to print same work process as a calculator use operators.

def calculator(a , b , op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b!=0:
            return a / b
        else:
            return "ERROR"
    else:
        return [::-1,"op Error"]
print(calculator(10 , 1 ,"="))


def flux(g):
    return g[::-1]
print(flux("Thakursab"))