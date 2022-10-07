
'''
7. Ask user to input email and check if the email is in valid form or not. 
Ex: it should contain single '@', '.', @or.shouldn't be in 1st position

'''

def check(mail):
    special_char=["@","."]
    for i in special_char:
        if i not in mail:
            print("Invalid emailId!!")
            return
        if mail[0]==i:
            print("Invalid emailId!!")
            return
    else:
        print("Valid emailID!!!")
mail=input("Enter a Email: ")
check(mail)
