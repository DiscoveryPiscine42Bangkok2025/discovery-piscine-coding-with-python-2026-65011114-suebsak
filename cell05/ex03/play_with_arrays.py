#!/usr/bin/env python3


original_array = [2, 8, 9, 48, 8, 22, -12, 2]


filtered_and_added = [x + 2 for x in original_array if x > 5]
unique_results = set(filtered_and_added)

print(original_array)
print(unique_results)