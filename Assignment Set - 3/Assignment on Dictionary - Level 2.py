Link : https://infytq.onwingspan.com/en/viewer/hands-on/lex_auth_01269444890062848087_shared?collectionId=lex_auth_0125409616243425281061_shared&collectionType=Course

Problem Statement : Write a python function, find_correct() which accepts a dictionary and returns a list as per the rules mentioned below.
The input dictionary will contain correct spelling of a word as key and the spelling provided by a contestant as the value.
The function should identify the degree of correctness as mentioned below:
CORRECT, if it is an exact match
ALMOST CORRECT, if no more than 2 letters are wrong
WRONG, if more than 2 letters are wrong or if length (correct spelling versus spelling given by contestant) mismatches and return a list containing the number of CORRECT answers, number of ALMOST CORRECT answers and number of WRONG answers.
Assume that the words contain only uppercase letters and the maximum word length is 10.

                                       Sample Input                                                         Expected Output

{"THEIR": "THEIR", "BUSINESS": "BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}                [2, 2, 1]

Solution :

def find_correct(word_dict):
    correct = 0
    almost_correct = 0
    wrong = 0
    count = 0
    keys = [i for i in word_dict.keys()]
    print(keys)
    values = [i for i in word_dict.values()]
    print(values)
    for i in range(len(keys)):
        if len(keys[i]) == len(values[i]) and keys[i] == values[i]:
           correct +=1
        elif len(keys[i]) != len(values[i]):
            wrong +=1
        else:
            for j in range(len(keys[i])) :
                if keys[i][j] != values[i][j]:
                    count += 1
            if count > 2:
                wrong+=1
            else:
                almost_correct+=1
        count = 0
    return [correct, almost_correct, wrong]


word_dict ={'MIND': 'MIME', 'WELL': 'WALL'}
print(find_correct(word_dict))
