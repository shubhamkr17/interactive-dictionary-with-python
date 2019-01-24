import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def meaning(word):
    word = word.lower()
    if word in data.keys():
        return data[word]
    elif len(get_close_matches(word,data.keys(),cutoff=0.8))>0 :
        match = get_close_matches(word,data.keys(),cutoff=0.8)[0]
        choice = input("Did you mean '%s' ??? \nEnter Y if Yes or N if No : " %match )
        if choice in ['Y','y']:
            return data[match]
        else :
            return "No such word exists!"
    else :
        return "No such word exists!"

query = input("Enter a word : ")

#printing the meaning 
output = meaning(query)
if type(output) ==  list :
    for item in output:
        print("# "+item)
else :
    print(output)