#!/usr/bin/env python3
import sys


if len(sys.argv) == 2:
    
    parameter = sys.argv[1]
    
    
    user_word = input("What was the parameter? ")
    
    
    if user_word == parameter:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    
    print("none")