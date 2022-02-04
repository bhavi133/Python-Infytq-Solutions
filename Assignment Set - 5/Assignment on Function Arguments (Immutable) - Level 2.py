Link : https://infytq.onwingspan.com/en/viewer/hands-on/lex_auth_01269441810970214471_shared?collectionId=lex_auth_012734003600908288382_shared&collectionType=Course

Problem Statement : Write a python function, check_double(number) which accepts a whole number and returns True if it satisfies the given conditions.
The number and its double should have exactly the same number of digits.
Both the numbers should have the same digits ,but in different order.
Otherwise it should return False.

Example: If the number is 125874 and its double, 251748, contain exactly the same digits, but in a different order.

Solution :

def check_double(number):
    square = number * 2
    number_sort = sorted(str(number))
    square_sort = sorted(str(square))
    if len(number_sort) == len(square_sort):
        if number_sort == square_sort:
            return True
        else:
            return False
    else:
        return False

# Provide different values for number and test your program
print(check_double(125874))
