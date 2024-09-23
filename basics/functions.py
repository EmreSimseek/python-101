#1 Basic Function Definition
def basic_function():
    print("This is a basic function.")

basic_function()

#2 Parameters and Default Values
def greet(name, greeting="Hello"):   #parameter with default value
    return f"{greeting}, {name}!"   

print(greet("Alice")) 
print(greet("Alex", "Good morning"))

#3 Keyword Arguments and Indefinite Number of Parameters
def flexible_function(*args,**kwargs):
    print("Positional arguments:",args) #pass arguments as a tuple
    print("Keyword arguments",kwargs)   #pass arguments as a key-value

flexible_function(1,2,3,"emre",False,name="alice",age=30) 



#4 Nested Functions
def outer_function(text):
    def inner_function():
        print(f"Inner: {text}")
    inner_function()

outer_function("Hello from outer function")

#5 Closure
def outer_function2(msg):
    def inner_function2():
        print(msg)
    return inner_function2

closure = outer_function2("Hello from closure!") 
closure() #Closure is when an inner function accesses and stores variables in the scope of an outer function.

#6 Lambda Functions

def square(x):      #Normal function definition
    return x**2              
# Same thing with lambda function
square_lambda = lambda x:x**2
#print(square(5)) #25
#print(square_lambda(5))  #25

numbers = [1,2,3,4,5]

doubled = map(lambda x: x*2,numbers)
#print(list(doubled))  #[2, 4, 6, 8, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
#print(evens)  # [2, 4, 6]

#7 Decorator
def decorator_function(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper
   
@decorator_function
def say_hello():
    print("Hello!")

say_hello()    


def repeat(n):
    def decorator(func):
        def wrapper():
            for _ in range(n):
                func()
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hi")

greet()

#8 Generators            
#Generators are able to navigate large data sets without keeping them in memory.
def simple_generator():
    yield 1
    yield 2
    yield 3
gen = simple_generator()
print(next(gen))
print(next(gen))
print(next(gen))

#9 recursive
def factorial(n):
    if n==1:
        return 1
    else:
        return n* factorial(n-1)
print(factorial(5))    #120
#10 Functions as High-Level Objects   
'''
In Python, functions are considered “first-class citizens”, meaning that they can be processed like any other data type,
assigned to a variable, passed as arguments to a function, or returned from another function.'''
def add(x,y):
    return x+y
def apply_function(func,x,y):
    return func(x,y)

result = apply_function(add,10,5)
print(result) #15   

#11 Documentation 
def multiply(x, y):
    """
    Multiplies two numbers and returns the result.
    :parameter x: First number
    :parameter y: Second number
    :return: Multiplication result
    """
    return x * y

#print(multiply.__doc__)  #docstrings that describe what the functions do.