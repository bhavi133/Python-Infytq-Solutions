Link : https://infytq.onwingspan.com/en/viewer/hands-on/lex_auth_012693797166096384149_shared?collectionId=lex_auth_0125409616243425281061_shared&collectionType=Course

Problem Statement : Write a Python program to generate the next 15 leap years starting from a given year. Populate the leap years into a list and display the list.

def find_leap_years(given_year):
    list_of_leap_years = []
    while len(list_of_leap_years) < 15:
        if (given_year % 400 == 0) and (given_year % 100 == 0):
            list_of_leap_years.append(given_year)
            given_year = given_year + 1
        elif (given_year % 4 == 0) and (given_year % 100 != 0):
            list_of_leap_years.append(given_year)
            given_year = given_year + 1
        else:
            given_year = given_year + 1
    return list_of_leap_years

list_of_leap_years=find_leap_years(2000)
print(list_of_leap_years)
