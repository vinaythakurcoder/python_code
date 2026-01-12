# write a function to print a return the sum of two numbers.

def sum_two_numbers(a, b):
    sum = a + b
    return sum  
print( sum_two_numbers(11, 25) )

# write a function to print and check if a number is even or odd.

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "odd"
print(check_even_odd(2))

# write a function to print and return the factorial of a number.

def factorial(n):
    result= 1
    while n > 1:
        result = result * n
        n = n - 1
    return result
print(factorial(5))

# write a function to print and return the largest numbers of the list.
def largest_number(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest
print(largest_number([10, 25, 5, 78, 99, 34]))

# write a function to print and return the prime numbers in a list.
  # step1:
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes

print(prime_numbers([2, 3, 4, 5, 6, 7, 8, 9, 10]))

  # step2: 

def print_prime_numbers(numbers):
    for num in numbers:
        if num > 1:          # Prime check 1 se bada hona chahiye
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(num)

print_prime_numbers([10, 2, 3, 4, 5, 6, 7, 11, 15, 17])
