#prime
'''
num=int(input("Enter a Number: "))

f=1
for i in range(2,num-1):
    if(num%i)==0:
        f=0;
        break;

if f==1:
    print(num," is a prime number")
else:
    print(num," is not a prime number")

'''
#prime in a range

start_no=int(input("Enter a starting of range: "))
end_no=int(input("Enter a end of range: "))
for j in range(start_no,end_no):
    f=1
    for i in range(2,j-1):
        if(j%i)==0:
            f=0;
            break;
    if f==1:
        print(j)
