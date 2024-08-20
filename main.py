import random
'''
1 for snake
-1 for water 
0 for gun
'''
Computer= random.choice([-1,0,1])
youstr = input("Enter your Choice:")
youDict = {"s": 1, "w" : -1, "g" : 0}
reversedict = {1:"snake", -1: "Water" , 0: "Gun"}
you = youDict[youstr]
print(f"You chose {reversedict[you]}\nComputer Chose {reversedict[Computer]}")
if(Computer == you):
    print("Its Draw")
else:
    if(Computer ==-1 and you ==1):
        print("You Win")
    elif(Computer ==-1 and you ==0):
        print("You Lose!")
    elif(Computer ==1 and you ==-1):
        print("you lose!")
    elif(Computer ==1 and you ==0):
        print("You win!")
    elif(Computer==0 and you ==-1):
        print("You Win!")
    elif(Computer ==0 and you ==1):
        print("You Lose!")
    else:
        print("Something Wrong")

