"""
3. Create a program to play RPS Game

Inputs:
1. Enter Player name 1
2. Enter Player name 2
3. Enter Player 1 Choice
4. Enter Player 2 Choice


Choices are "Rock", "Scissor", "Paper"

result: who wins?


display result: Player name with choice Rock wins
Player name with choice Scissor Lose


how to manipulate result:
If P1 enter Rock and P2 enters Scissor then P1 Wins
if P1 enter Rock and P2 enters Paper then P2 Wins
if P1 enter Scissor and P2 enters Paper then P1 wins
if both player enters the same choice it should say "Tie"

"""


name1=input("Enter Player name 1:")
name2=input("Enter Player name 2:")

choices=["rock", "scissor", "paper"]
print("choices are ",choices)

choice1=input("Enter Player 1 Choice:").lower()
choice2=input("Enter Player 2 Choice:").lower()

if(choice1=="rock" and choice2=="scissor")or(choice1=="scissor" and choice2=="paper")or (choice1=="paper" and choice2=="rock"):
    print(name1 ,"wins")
elif(choice1=="rock" and choice2=="paper")or(choice1=="paper" and choice2=="scissor")or (choice1=="scissor" and choice2=="rock"):
    print(name2 ,"wins")
else:
    print("Invalid choice")




