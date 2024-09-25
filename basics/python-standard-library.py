import os

# Learn the current working directory
print(os.getcwd())

# Create a new directory
#os.mkdir("yeni_klasor")
import sys

# Learn the version of the Python interpreter
print(sys.version)

# Accessing command line arguments
#print(f"File name:{sys.argv[0]} firs input:{sys.argv[1]}")

import datetime

# Current date and time
print(datetime.datetime.now())

# The difference between two dates
date1 = datetime.date(2023, 1, 1)
date2 = datetime.date(2024, 1, 1)
diff = date2 - date1
print(diff.days)  # Number of days between two dates

import random

# Generate a random number between 0 and 1
print(random.random())

# Select a random number from a given range
print(random.randint(1, 100))

# Randomly shuffle a list
list= [1, 2, 3, 4, 5]
random.shuffle(list)
print(list)

import json

# Convert Python dictionary to JSON format
data = {"name": "Emre", "age": 22}
json_data = json.dumps(data)
print(json_data)

# Convert from JSON format to Python data structure
python_data = json.loads(json_data)
print(python_data)

import re

# Search for a specific pattern in a text
text = "Hello, my name is Osipov."
pattern = r"my name is (\w+)"
result = re.search(pattern,text)

# Print the result on the screen if there is a match
if result:
    print(f"Found name: {result.group(1)}")
    

import time

# Learning the current time
print(time.time())

# Waiting 2 seconds
time.sleep(2)
print("2 seconds passed.")

import itertools

# Creating permutations
permutations = itertools.permutations([1, 2, 3])
for p in permutations:
    print(p)  

import functools

# Caching the result of a function
@functools.lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Fibonacci calculation
print(fibonacci(10))      