#1 Importing Modules
import math # Import All Module
print(math.sqrt(16))

from math import factorial # Importing a Specific Part from a Module
print(factorial(5))

import math as m # Renaming Modules
print(m.pow(2,3))

from math import *  #Importing All Content 
print(sin(0))
print(pi)

#2 Creating Our Own Modules
import functions
print(functions.basic_function())


#3 Modules Loading Order and Path
import sys
print(sys.path) 
'''This list contains the following:
The directory of the currently running Python script.
Python's standard library directories.
Additional paths specified by Python's PYTHONPATH environment variable.
'''

