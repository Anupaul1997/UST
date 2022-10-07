"""

8. Write a pay computation program with time-and-a-half for overtime and create a function called computepay which takes two parameters
 (hours and rate).
8 hours * 5 days = 40 hours , 5 hours = 1.5 times

Enter Hours: 45
Enter Rate: 10
Pay: 475.0

Write functions to calculate your trip's costs:

Define a function called hotel_cost with one argument nights as input. The hotel costs $140 per night. 
So, the function hotel_cost should return 140 * nights.

Define a function called plane_ride_cost that takes a string, city, as input. The function should return a different price depending on 
the location, similar to the code example above. Below are the valid destinations and their corresponding round-trip prices.
"Charlotte": 183
"Tampa": 220
"Pittsburgh": 222
"Los Angeles": 475

define a function called rental_car_cost with an argument called days. Calculate the cost of renting the car: 
Every day you rent the car costs $40.(cost=40*days)
 if you rent the car for 7 or more days, you get $50 off your total(cost-=50).
  Alternatively (elif), if you rent the car for 3 or more days, you get $20 off your total. 
  You cannot get both of the above discounts. Return that cost.

Then, define a function called trip_cost that takes two arguments, city and days.
 Like the example above, have your function return the sum of calling the rental_car_cost(days),
  hotel_cost(days), and plane_ride_cost(city) functions.

Modify your trip_cost function definion. Add a third argument, spending_money. 
Modify what the trip_cost function does. Add the variable `spending_money to the sum that it returns
"""
def computepay(hour,rate):
    pay=(hour*rate)+((hour%40)*(rate*1/2))
    return pay
        

hour=int(input("Enter hour:"))
rate=int(input("Enter rate:"))
print("Total pay: ",computepay(hour,rate))



def hotel_cost(night):
    return 140*night

def plane_ride_cost(city):
    price_list={"Charlotte": 183,"Tampa": 220,"Pittsburgh": 222,"Los Angeles": 475}
    return price_list[city]

def rental_car_cost(days):
    cost=40*days
    if (days>=7):
        cost-=50
    elif (days>=3):
        cost-=20
    return cost

def trip_cost(city,days):
    return rental_car_cost(days)+ hotel_cost(days)+ plane_ride_cost(city)

def trip_cost(city,days,spend_money=None):
    if(spend_money!=None):
        return rental_car_cost(days)+ hotel_cost(days)+ plane_ride_cost(city)+spend_money
    else:
        return rental_car_cost(days)+ hotel_cost(days)+ plane_ride_cost(city)



days=int(input("Enter the trip days: "))
print("enter the city name you going to visit:")
city=input("Charlotte , Tampa , Pittsburgh , Los Angeles:  ")
print("Total cost: ",trip_cost(city,days))
spend_money= int(input("Enter the spending cost:"))
print("Total cost: ",trip_cost(city,days,spend_money))