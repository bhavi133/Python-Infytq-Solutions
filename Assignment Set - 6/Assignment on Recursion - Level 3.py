Link : https://infytq.onwingspan.com/en/viewer/hands-on/lex_auth_01269443477535129681_shared?collectionId=lex_auth_012734003600908288382_shared&collectionType=Course
    
Problem Statement : Write a python function find_duplicates(), which accepts a list of numbers and returns another list containing all the duplicate values in the input list and the order should be same as in the input list. If there are no duplicate values, it should return an empty list.

           Sample Input                    Expected Output

[12,54,68,759,24,15,12,68,987,758,25,69]      [12, 68]

Solution :
  
def find_duplicates(list_of_numbers):
    #start writing your code here
    return [i for i in set(list_of_numbers) if list_of_numbers.count(i) > 1]
            
list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)
