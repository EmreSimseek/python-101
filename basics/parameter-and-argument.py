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

print(greet())       
print(greet("Alex")) 
#Default parameters must always follow mandatory parameters. Otherwise we get an error

#Keyword Arguments
def introduce(name,age):
    return f"Hello, my name is {name} and I am {age} years old"

print(introduce("Bob",30))
print(introduce(age=25,name="Alex")) #Call with keyword arguments
