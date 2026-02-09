#!/usr/bin/env python3
import math

try:
    
    user_input = input("Give me a number: ")
    number = float(user_input)

    
    result = math.ceil(number)

    
    print(result)

except ValueError:
    print("Error: Please enter a valid number.")