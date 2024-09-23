def basic_function():
    print("This is a basic function.")

basic_function()

def greet(name, greeting="Hello"):   #parameter with default value
    return f"{greeting}, {name}!"   

print(greet("Alice")) 
print(greet("Alex", "Good morning"))

def flexible_function(*args,**kwargs):
    print("Positional arguments:",args) #pass arguments as a tuple
    print("Keyword arguments",kwargs)   #pass arguments as a key-value

flexible_function(1,2,3,"emre",False,name="alice",age=30) 


def outer_function(text):
    def inner_function():
        print(f"Inner: {text}")
    inner_function()

outer_function("Hello from outer function")          