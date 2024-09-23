# Basic Use
def greet():
    return "Hello World"
message = greet()
print(message)

# Returning a Value from a Function
def get_even_numbers(n):
    even_numbers = []
    for i in range(n):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers
print(get_even_numbers(5))

# Returning More Than One Value from a Function
def get_full_name():
    first_name = "Lionel"
    last_name =   "Messi"
    return first_name , last_name
 
fname,lname = get_full_name()
print(f"First Name: {fname}")  
print(f"Last Name: {lname}")

# Stop Function Operation
def process_data(data):
    if not data:
        print("No data provided.")
        return #function stop here
    print(f"Processing {len(data)} items")

process_data([])
process_data([1,2,3])

# Functions that Return No Value
def say_hello(name):
    print(f"Hello, {name}")

result = say_hello("Emre")
print(result)  #None   

# Return and Loops
def find_first_even(numbers):
    for num in numbers:
        if num % 2 ==0:
            return num
    return None

print(find_first_even([1, 3, 5, 6, 7]))  # Output:6
print(find_first_even([1, 3, 5]))        # Output:None

# Return in Recursive Functions
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)  
print(fibo(5))

