#Ques1
a=4
b=3
print("Orginal value :",a," and ",b)

b=a+b
a=b-a
b=b-a

print("Swapped value :",a," and ",b)

# #Ques 2

no_of_apples=100
print("Number of apples :",no_of_apples)

price_of_apple=7.5
print("Price of apple :",price_of_apple)

total_amount_of_apples=no_of_apples*price_of_apple
print("Amount of apples :",total_amount_of_apples)

no_sold_apples=20
price_of_apple=10
total_1=no_sold_apples*price_of_apple
print("After sold 20 apples for 10 rs he get :",total_1)

no_sold_apples=30
price_of_apple=50
total_2=no_sold_apples*price_of_apple
print("After sold 30 apples for 50 rs he get :",total_2)

grand_total=total_1+total_2
print("Total amount he get :",grand_total)

profit_or_loss=grand_total-total_amount_of_apples

print("profit :",profit_or_loss)

#ques 3

print("Shopkeeper can buy :",profit_or_loss//price_of_apple," apples from his earning")
    



