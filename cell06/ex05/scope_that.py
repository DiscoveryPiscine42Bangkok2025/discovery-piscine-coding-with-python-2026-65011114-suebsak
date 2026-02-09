#!/usr/bin/env python3


def add_one(value):
   
    value += 1

def main():
    
    my_var = 10
    
    
    print(f"Before call: {my_var}")
    
    
    add_one(my_var)
    
    
    print(f"After call: {my_var}")

if __name__ == "__main__":
    main()