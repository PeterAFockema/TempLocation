#convert_string_to_a_list_of_characters.py

character_string = "character"
#Method 1: Iterate through the string using a for loop
character_list = []
for character in character_string:
    character_list.append(character)
print(character_list)
#Method 2: Use List comprehension
character_list = [char for char in character_string]
print(character_list)
