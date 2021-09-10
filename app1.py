import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w] 
    elif w.upper() in data:
        return data[w]      
    elif len(get_close_matches(w,data.keys()))>0:
        yn=input("did you mean %s instead?Enter Y if yes,N if no." %get_close_matches(w,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="N":
            return "the word doesnt exist.please double check"
        else:
            return "we didnt get your response."


    else:
        return "the word doesn't exist.Please double check it."

word=input("enter a word: ")

meaning=translate(word)

if type(meaning)==list:
    for item in meaning:
        print(item)
 
else:
    print(meaning)




