#!/usr/bin/env python3
import sys


def downcase_it(string_in):
    return string_in.lower()

def main():
    
    if len(sys.argv) > 1:
        
        for arg in sys.argv[1:]:
            
            print(downcase_it(arg))
    else:
        
        print("none")

if __name__ == "__main__":
    main()