Link : https://infytq.onwingspan.com/en/viewer/hands-on/lex_auth_01269442114344550475_shared?collectionId=lex_auth_012734003600908288382_shared&collectionType=Course
    
Problem Statement : Write a recursive function, is_palindrome() to find out whether a string is a palindrome or not. The function should return true, if it is a palindrome. Else it should return false. 
Note- Perform case insensitive operations wherever necessary.

Solution : 
  
def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

# Provide different values for word and test your program
result = is_palindrome("MadAMa")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")
