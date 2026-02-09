#!/usr/bin/env python3
import sys


if len(sys.argv) == 3:
    try:
        
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        
        
        result = list(range(start, end + 1))
        
        
        print(result)
        
    except ValueError:
        
        print("none")
else:
    
    print("none")