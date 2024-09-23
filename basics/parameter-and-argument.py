def greet(name):  # name is a parameter here
    return f"Hello, {name}!"

greet("Messi") # Messi is an argument here

#Positional Parameters
def add(a,b):
    return a+b

result = add(5,3)  #if we do not give arguments to the mandatory parameters we will get an error

#Default Parameters
def greet2(name="Guest"):
    return f"Hello, {name}!"

print(greet2())       
print(greet2("Alex")) 
#Default parameters must always follow mandatory parameters. Otherwise we get an error

#Keyword Arguments
def introduce(name,age):
    return f"Hello, my name is {name} and I am {age} years old"

print(introduce("Bob",30))
print(introduce(age=25,name="Alex")) #Call with keyword arguments

#Flexible Parameters
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3, 4))

def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_info(name="Alice", age=30, city="New York")

def example_func(a,b=10,*args,**kwargs):
    print(f"a:{a}, b:{b}")
    print(f"args:{args}")
    print(f"kwargs:{kwargs}")
    
example_func(1,2,3,4,name="Alex",age=30)

def add2(a,b,c):
    return a+b+c
nums = [1,2,3]
print(add2(*nums))

def greet3(name,age):
    return f"{name} is {age} years old"
info = {"name":"Messi", "age":38}
print(greet3(**info))

def append_item(item, item_list=None):
    if item_list is None:
        item_list = []
    item_list.append(item)
    return item_list

print(append_item(1)) 
print(append_item(2))
    