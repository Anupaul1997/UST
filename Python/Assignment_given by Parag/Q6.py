"""
6. Ask user a input string and check if the entered string is palindrome. Ex: Input NitiN -> o/p palindrome
"""

str=input("Enter a string: ")
if(str==str[::-1]):
    print(str," is a palindrome")
else:
    print(str," is not a palindrome")

