Link : https://infytq.onwingspan.com/en/viewer/hands-on/lex_auth_01269444961482342489_shared?collectionId=lex_auth_0125409616243425281061_shared&collectionType=Course

Problem Statement : Write python function, sms_encoding() which accepts a sentence and converts it into an abbreviated sentence to be sent as SMS and returns the abbreviated sentence. 
Rules are as follows: 
a. Spaces are to be retained as is 
b. Each word should be encoded separately
  If a word has only vowels then retain the word as is
  If a word has a consonant (at least 1) then retain only those consonants
Note: Assume that the sentence would begin with a word and there will be only a single space between the words.

Sample Input                                     Expected Output

I love Python                                    I lv Pythn   

I will not repeat mistakes                       I wll nt rpt mstks

MSD says I love cricket and tennis too           MSD sys I lv crckt nd tnns t

Solution : 

def sms_encoding(data):
    a = data.split()
    string = ""
    vowels = ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]
    for i in a:
        if len(i) < 2 :
            string = string + " "
            string = string + i 
        else:
            string = string + " "
            for j in i:
                if  j not in vowels:
                    string = string + j  
                else:
                    pass
    return string.strip()

data="I love Python"
print(sms_encoding(data))
