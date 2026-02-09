#!/usr/bin/env python3
import sys


def shrink(s):
    print(s[:8])


def enlarge(s):
    padding = 'Z' * (8 - len(s))
    print(s + padding)

def main():
    
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            length = len(arg)
            
            if length > 8:
                shrink(arg)
            elif length < 8:
                enlarge(arg)
            else:
                
                print(arg)
    else:
        print("none")

if __name__ == "__main__":
    main()