Link : https://infytq.onwingspan.com/en/viewer/hands-on/lex_auth_012693802383794176153_shared?collectionId=lex_auth_0125409616243425281061_shared&collectionType=Course

Problem Statement : Write a python function to check whether three given numbers can form the sides of a triangle.
Hint: Three numbers can be the sides of a triangle if none of the numbers are greater than or equal to the sum of the other two numbers.
  
Solution : 
  
def form_triangle(num1,num2,num3):
    # Do not change the messages provided below
    success="Triangle can be formed"
    failure="Triangle can't be formed"

    # Write your logic here

    # Use the following messages to return the result wherever necessary
    if num1 < (num2 + num3) and num2 < (num1 + num3) and num3 < (num2 + num1):
        return success
    else:
        return failure

# Provide different values for the variables, num1, num2, num3 and test your program
num1=3
num2=3
num3=5
form_triangle(num1, num2, num3)
