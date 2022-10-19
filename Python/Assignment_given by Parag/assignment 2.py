
#Ques 1

num=int(input("Enter a number :"))
if(num%2==0):
    print("Number ",num," is even")
else:
    print("Number ",num," is odd")


#Ques 2

degree=int(input("Degree :"))
type=input("type: ")
if('C'in type or 'c' in type):
    F=degree*(9/5)+32
    print(degree," celcius = ",int(F)," Fahrenheit")

elif('F'in type or 'f' in type):
    C=(degree-32)*5/9
    print(degree," Fahrenheit = ",int(C)," Celcius")

else:
    print("Invalid input")



#Ques 3


l=int(input("Enter the length in inches :"))
meters=l//39.37
cm=(l%39.37)*2.54
print(l," inches = ",int(meters)," meters and ",int(cm),"centimeters")



