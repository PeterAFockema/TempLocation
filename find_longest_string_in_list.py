#find_longest_string_in_list.py

#Method 1: Iterate through the list using a loop
# and keep track of the longest string
string_list = ["hello", "world", "let's", "learn", "some", "Python"]
longest = ""
for current_string in string_list:
    if len(current_string) > len(longest):
        longest = current_string
print(longest)

#Method 2: Iterate through the list using a functional approach
import functools
functools.reduce(lambda longest, current_string:
        current_string if len(current_string) > len(longest) else longest, string_list, "")
print(longest)
