import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def meaning(word):
    word = word.lower()
    if word in data.keys():
        return data[word]
    elif len(get_close_matches(word,data.keys(),cutoff=0.8))>0 :
        return "Did you mean '%s' ???" % get_close_matches(word,data.keys(),cutoff=0.8)[0]
    else :
        return "No such word exists"

query = input("Enter a word : ")
print(meaning(query))