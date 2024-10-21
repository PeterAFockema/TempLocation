#find_non_repeating_characters_in_list.py

#Take the user input
String = "prepinsta"

for i in String:
    #print(i)
    #Initialise a count variable
    count = 0
    for j in String:
        #Check for repeated characters
        if i == j:
            count += 1
        #If character is found >1 time, then break the loop
        if count >1:
            break
    #Print for the non-repeating characters
    if count == 1:
        print(i, end = " ")

for i in String:
    if String.count(i) == 1:
        print("i #2 method non-repeating character is: ", i)
