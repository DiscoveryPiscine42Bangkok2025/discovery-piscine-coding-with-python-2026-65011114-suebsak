#!/usr/bin/env python3


def famous_births(scientists):
    
    sorted_scientists = sorted(scientists.values(), key=lambda x: x['date_of_birth'])
    
    for person in sorted_scientists:
        name = person['name']
        birth_year = person['date_of_birth']
        print(f"{name} is a great scientist born in {birth_year}.")

def main():
    
    women_scientists = {
        "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
        "cecilia": { "name": "Cecilia Payne", "date_of_birth": "1900" },
        "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
        "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
    }
    
    famous_births(women_scientists)

if __name__ == "__main__":
    main()