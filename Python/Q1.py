""""
1. Write a function to take input from user in days and print it in years, month and days
input - 397, output - 1 year , 1 month , 1 day

"""


def check(input_value):
    yr=input_value//365
    month=(input_value-(yr*365))//31
    day=input_value-(yr*365)-(month*31)
    return yr,month,day


d = int(input("Number of days: "))
yr,month,day=check(d)
print(yr," year , ",month," month , ",day," day")

