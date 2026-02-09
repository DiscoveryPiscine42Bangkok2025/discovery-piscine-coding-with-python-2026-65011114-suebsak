#!/usr/bin/env python3
import sys


if len(sys.argv) == 2:
    text = sys.argv[1]
    
    results = [char for char in text if char == 'z']
    
    
    if results:
      
        print("".join(results))
    else:
      
        print("none")
else:
    
    print("none")