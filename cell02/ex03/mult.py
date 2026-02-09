#!/usr/bin/env python3

try:
    
    print("Enter the first number:")
    num1 = float(input())
    
    print("Enter the second number:")
    num2 = float(input())

   
    result = num1 * num2

    
    display_num1 = int(num1) if num1.is_integer() else num1
    display_num2 = int(num2) if num2.is_integer() else num2
    display_result = int(result) if result.is_integer() else result
    
    print(f"{display_num1} x {display_num2} = {display_result}")

    
    if result > 0:
        print("The result is positive.")
    elif result < 0:
        print("The result is negative.")
    else:
        
        print("The result is positive and negative.")

except ValueError:
    print("Invalid input. Please enter valid numbers.")