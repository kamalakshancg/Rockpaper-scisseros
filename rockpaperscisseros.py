import random
def welcome():
        for i in range(0,10):
            print("*\t",end=" ")
        print()
        print("*",end=" ")
        for i in range(1,10):
            print("\t",end=" ")
        print("*")
        print("*",end=" ")
        for i in range(1,10):
            print("\t",end=" ")
        print("*")
        print("*",end="")
        for i in range(0,4):
            print("\t",end="")
        print("welcome to game",end="")
        for i in range(0,4):
            print("\t",end=" ")
        print("*")
        print("*",end="")
        for i in range(1,10):
            print("\t",end=" ")
        print("*")
        print("*",end="")
        for i in range(1,10):
            print("\t",end=" ")
        print("*")
        print("*",end="")
        for i in range(1,10):
            print("\t",end=" ")
        print("*")
        for i in range(0,10):
            print("*\t",end=" ")
        print()
        input("enter any key to start the game: ")
def mainmenu():
    print("1.Rock paper Scisseros \t  2.Numberguess \n")
    ch=int(input("Select the Game:"))
    if ch==1:
        RockpaperScisserormenu()
    elif ch==3:
        exit()
    else:
        print("Enter the valid game number")
        mainmenu()     
 def RockpaperScisserormenu():
    print("1.Play \n 2.Rules \n 3.Exit")
    ch=int(input("Enter the choice"))
    if ch==1:
        Rockpaperscissers()
    elif ch==2:
        RockpaperscissersRules()
    elif ch==3:
        mainmenu()
    else:
        print("Invalid number")
        RockpaperScisserormenu()
        
def RockpaperscissersRules():
    print("If your choice is Rock, please enter  0\n")
    print("If your choice is paper, please enter  1\n")
    print("If your choice is scissers, please enter  2\n")
def Rockpaperscissers():
    print("let's start the game \n")
    print("If your choice is Rock, please enter  0\n")
    print("If your choice is paper, please enter  1\n")
    print("If your choice is scissers, please enter  2\n")
    user=0
    comp=0
    count=0
    choice=['Rock',"paper","scisseros"]
    while user<5 and comp<5:
        count+=1
        if count==2:
            mainmenu()
        u_ch=int(input("Enter the choice"))
        if u_ch==-1:
            print("exiting from the game")
            return
        c_ch=random.choice([0,1,2])
        if u_ch==0 and c_ch==1:
            comp+=1
        elif u_ch==0 and c_ch==2:
            user+=1
        elif u_ch==1 and c_ch==0:
            comp+=1
        elif u_ch==1 and c_ch==2:
            user+=1
        elif u_ch==2 and c_ch==0:
            comp+=1
        elif u_ch==2 and c_ch==1:
            user+=1
        print("you",choice[u_ch])
        print("computer",choice[c_ch])
        print("user score",user,"computer score",comp)
    if user>comp:
        print("\n congrates you won")
    elif comp>user:
        print("\n sorry you lost")
    else:
        print("\n match tied")
 welcome()
print("\n"*100)
mainmenu()
