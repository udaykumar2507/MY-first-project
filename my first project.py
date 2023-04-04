import random
list=["stone","paper","scissors"]
i=1
round =0
win=0
while(i<=5):
    user=input("ENTER STONE OR PAPER OR SCISSOR :")
    comp=(random.choice(list))
    print("OPPONENT :",comp)
    if user=="stone" and comp=="scissors":
        print("WON")
        win+=1
    elif user=="stone" and comp =="paper":
        print("LOSS")
    elif  user=="scissors" and comp=="paper":
        print("WON")
        win+=1
    elif user=="scissors" and comp=="stone":
        print("LOSS")
    elif user=="paper" and comp=="stone":
        print("WON")
        win+=1
    elif user=="paper" and comp=="scissors":
        print("LOSS")
    elif user==comp:
        print("DRAW")
    i+=1
    round+=1
    print("ROUND",round)
    print("CHANCE LEFT",6-i)
if win>=3:
    print("                                 HEYYYYYYY YOU WON                            ")
elif win<3:
    print("                                  OOPS YOU LOSSS                                      ")