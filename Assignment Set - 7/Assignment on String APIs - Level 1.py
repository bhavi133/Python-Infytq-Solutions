Link : https://infytq.onwingspan.com/en/viewer/hands-on/lex_auth_01269446319507046499_shared?collectionId=lex_auth_012734003600908288382_shared&collectionType=Course
    
Problem Statement : Write a python function, remove_duplicates() which accepts a string and removes all duplicate characters from the given string and return it.

       Sample Input              Expected Output
1122334455ababzzz@@@123#*#*         12345abz@#*

Solution : 

def remove_duplicates(value):
    # start writing your code here
    string = ""
    for i in value:
        if i not in string:
            string = string + i
    return string
    
print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))
