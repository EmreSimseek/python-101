#1 Local Variables
def my_function():
    x=10
    print(f"Local x:{x}")

my_function()
#print(x)  NameError: name 'x' is not defined       

#2 Global Variable
y=20
def my_function2():
    
    global y #Accessing Global Variables Inside a Function
    y+=10  
    print(f"Global y with addition:{y}")

my_function2()
print(f"Global y is out:{y}")   

#3 Global and Local Variable with Same Name in Function
b = 50 
def my_function():
    b = 10  
    print(f"Lokal b: {b}")

my_function()  # b:10
print(f"Global b: {b}")  # b:50

#4 Global and Nonlocal Difference
def outer_function():
    x = "outer"

    def inner_function():
        nonlocal x    # Accessing outer scope variables
        x = "inner"
    
    inner_function()
    print(f"Outer x: {x}")

outer_function()  