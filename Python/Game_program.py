#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def game(choice1,choice2):
    if (choice1=="snake" and choice2=="water") or (choice1=="gun" and choice2=="snake") or(choice1=="water" and choice2=="gun"):
        print("player1 wins")
        return "p1"
    elif(choice2=="snake" and choice1=="water") or (choice2=="gun" and choice1=="snake") or(choice2=="water" and choice1=="gun"):
        print("player2 wins")
        return "p2"
    else:
        print("Invalid choice Or tie occured")
        return False
    
no_turn=int(input("Enter number of turn: "))
p1=0
p2=0
for i in range(no_turn):
    choice1=input("Enter player1 choice: ").lower()
    choice2=input("Enter player2 choice: ").lower()
    result=game(choice1,choice2)
    if (result):
        if result=="p1":
            p1+=1
        elif result=="p2":
            p2+=1
    
        

print("Score")
print("=======================")
print("player1 \tplayer2 ")
print(p1,"\t\t",p2 )
        
    

