#!/usr/bin/env python3

try:
    
    print("Enter a number")
    user_input = input()
    number = int(user_input)

   
    for i in range(10):
        result = i * number
        
        print(f"{i} x {number} = {result}")

except ValueError:
    print("Error: Please enter a valid integer.")