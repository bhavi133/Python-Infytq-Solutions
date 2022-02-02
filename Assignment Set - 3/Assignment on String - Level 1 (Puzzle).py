Link : https://infytq.onwingspan.com/en/viewer/hands-on/lex_auth_012693825794351104168_shared?collectionId=lex_auth_0125409616243425281061_shared&collectionType=Course

Problem Statement : Write a python program to display all the common characters between two strings. Return -1 if there are no matching characters.
Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.

         Sample Input                          Expected output

        "I like Python"
                                                   lieyon
"Java is a very popular language"

Solution : 
  
def find_common_characters(msg1, msg2):
    string = ""
    for i in msg1:
        if i in msg2 and i != " " and i not in string:
            string = string + i
    if len(string) == 0:
        return -1
    else:
        return string

# Provide different values for msg1,msg2 and test your program
msg1 = "I like Python"
msg2 = "Java is a very popular language"
common_characters = find_common_characters(msg1, msg2)
print(common_characters)
