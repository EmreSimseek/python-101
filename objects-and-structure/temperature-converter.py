def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5 / 9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9 / 5 + 32

def convert_temperature(value, unit_from, unit_to):
    if unit_from == 'C':
        if unit_to == 'F':
            return celsius_to_fahrenheit(value)
        elif unit_to == 'K':
            return celsius_to_kelvin(value)
    elif unit_from == 'F':
        if unit_to == 'C':
            return fahrenheit_to_celsius(value)
        elif unit_to == 'K':
            return fahrenheit_to_kelvin(value)
    elif unit_from == 'K':
        if unit_to == 'C':
            return kelvin_to_celsius(value)
        elif unit_to == 'F':
            return kelvin_to_fahrenheit(value)
    return None  # Invalid conversion

while True:
    unit_from = input("Enter the temperature unit to convert from (C/F/K or 'q' to quit): ").upper()
    
    if unit_from == 'Q':  # Exit option
        print("Exiting the program.")
        break

    if unit_from not in ['C', 'F', 'K']:
        print("Invalid unit. Please enter C, F, or K.")
        continue

    try:
        temperature = float(input("Enter the temperature value: "))
    except ValueError:
        print("Invalid temperature value. Please enter a valid number.")
        continue

    unit_to = input("Enter the unit to convert to (C/F/K): ").upper()
    
    if unit_to not in ['C', 'F', 'K']:
        print("Invalid unit. Please enter C, F, or K.")
        continue

    if unit_from == unit_to:
        print("No conversion needed. The temperature is the same.")
        continue

    converted_temperature = convert_temperature(temperature, unit_from, unit_to)

    if converted_temperature is not None:
        print(f"{temperature:.2f}{unit_from} is equal to {converted_temperature:.2f}{unit_to}")
    else:
        print("Invalid conversion. Please try again.")
    
  
