#!/usr/bin/env python3


def array_of_names(persons):
    full_names = []
    
    for first, last in persons.items():
        
        formatted_name = f"{first.capitalize()} {last.capitalize()}"
        full_names.append(formatted_name)
    
   
    return full_names

def main():
   
    persons = {
        "somsir": "jundee",
        "somchai": "madee",
        "somsak": "punmee",
        "somjai": "maitree"
    }
    
    
    print(array_of_names(persons))

if __name__ == "__main__":
    main()