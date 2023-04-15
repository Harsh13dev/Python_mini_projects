import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def search(word):
    word = word.lower()                                                                      # Convert all letters to lower case
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]                                                            # If the first letter is capital
    elif word.upper() in data:
        return data[word.upper()]                                                            # If the word is in upper case in data.json file
    elif len(get_close_matches(word, data.keys())[0]) > 0:
        print("Did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("Press y for YES or n for NO:")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            print("You have entered a wrong word or the word dose not exist")
        else:
            print("Please enter y or n")
    else:
        print("You have entered a wrong word or the word dose not exist")


word = input("Enter the word to search:")
output = search(word)

if type(output) == list:                                                                     # For interface.If there exist more than one definations of a word
    for items in output:                                                                     # Put every defination in new line
        print("*", items)
else:
    print(output)

