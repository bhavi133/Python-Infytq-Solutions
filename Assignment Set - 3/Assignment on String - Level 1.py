Link : https://infytq.onwingspan.com/en/viewer/hands-on/lex_auth_012693819159732224162_shared?collectionId=lex_auth_0125409616243425281061_shared&collectionType=Course

Problem Statement : Write a function, check_palindrome() to check whether the given string is a palindrome or not. The function should return true if it is a palindrome else it should return false.
Note: Initialize the string with various values and test your program. Assume that all the letters in the given string are all of the same case. Example: MAN, civic, WOW etc.

Solution : 
  
def check_palindrome(word):
    return word == word[::-1]
    # Remove pass and write your logic here

status = check_palindrome("malayalam")
if (status):
    print("word is palindrome")
else:
    print("word is not palindrome")
