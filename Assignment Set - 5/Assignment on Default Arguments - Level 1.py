Link : https://infytq.onwingspan.com/en/viewer/hands-on/lex_auth_0127382164803993601239_shared?collectionId=lex_auth_012734003600908288382_shared&collectionType=Course

Problem Statement : Consider sample data as follows: sample_data=range(1,11)
Create two functions: odd() and even()
The function even() returns a list of all the even numbers from sample_data
The function odd() returns a list of all the odd numbers from sample_data

Create a function sum_of_numbers() which will accept the sample data and/or a function.
If a function is not passed, the sum_of_numbers() should return the sum of all the numbers from sample_data
If a function is passed, the sum_of_numbers() should return the sum of numbers returned from the function passed.

Solution :

def sum_of_numbers(list_of_num,filter_func=None):
    if filter_func == even:
        return sum(even(list_of_num))
    elif filter_func == odd:
        return sum(odd(list_of_num))
    else:
        return sum(list_of_num)

def even(data):
    return [i for i in data if  i % 2 == 0]

def odd(data):
     return [i for i in data if  i % 2 == 1]

sample_data = range(1,11)
print(sum_of_numbers(sample_data,None))
