from difflib import get_close_matches
import json
data = json.load(open("data.json"))

def search(word):
    if word in data:
        
        result= data[word]
        if len(result)>0:
            if len(result)==1:
                return result
            else:
                for i in range(0,len(result)-1):
                    print (result[i], "/n")
                return (result[i+1])

            
    elif len(get_close_matches(word,data.keys())) > 0:
        print ("Did you mean: " , get_close_matches(word,data.keys())[0])
        decision = input("Enter Y if yes, N if no: ")
        if decision == "Y":
            result = data[get_close_matches(word,data.keys())[0]]
            if len(result)>0:
                if len(result)==1:
                    return result
                else:
                    for i in range(0,len(result)-1):
                        print (result[i], "/n")
                    return (result[i+1])
        elif decision == "N":
            return ("Sorry, I'm unable to find the word that you were searchning for")
    else:  
        return ("Sorry, I'm unable to find the word that you were searchning for")

word=input("Enter the word to search: ")
word = str.lower(word)
print(search(word))