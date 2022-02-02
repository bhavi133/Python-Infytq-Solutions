Link : https://infytq.onwingspan.com/en/viewer/hands-on/lex_auth_01269441913243238467_shared?collectionId=lex_auth_0125409616243425281061_shared&collectionType=Course

Problem Statement : Write a python function, create_largest_number(), which accepts a list of numbers and returns the largest number possible by concatenating the list of numbers.
Note: Assume that all the numbers are two digit numbers.
  
Sample Input   Expected Output
  23,34,55         553423

Solution : 
  
def create_largest_number(number_list):
    number_list = sorted(number_list, reverse=True)
    string = ""
    for i in number_list:
        string = string + str(i)
    return int(string)
    # remove pass and write your logic here

number_list = [23, 45, 67]
largest_number = create_largest_number(number_list)
print(largest_number)
