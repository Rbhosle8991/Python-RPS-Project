# rock =1
# paper=0
# scissor=-1

import random

computer = random.choice([1,0,-1])

youstr = input("Enter your choice : ")
youdict = {"r":1 , "p":0 , "s":-1}
reversedict = {1:"rock" , 0:"paper" , -1:"scissor"}
you =youdict[youstr]

print("You chose : " , reversedict[you])
print("Computer Chose : " , reversedict[computer])

if(computer==you):
    print("It's a tie")

else:
    if(computer==1 and you==0):
        print("you win")

    elif(computer==1 and you==-1):
        print("Computer win")

    elif(computer==0 and you==1):
        print("Computer win")

    elif(computer==0 and you==-1):
        print("you win")

    elif(computer==-1 and you==1):
        print("you win")

    elif(computer==-1 and you==0):
        print("Computer win") 

    else:
        print("Something went wrong")





