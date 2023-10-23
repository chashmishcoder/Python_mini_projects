def sps():
    print("Rules of Game\n")
    print("1- Stone")
    print("2- Paper")
    print("3- Scissor\n")
    print("Player 1 : Enter your Choice")
    p1 = int(input())
    print("Player 2 : Enter your Choice")
    p2 = int(input())

    if (p1 == 1 and p2 == 3) or (p1 == 2 and p2 == 1) or (p1 == 3 and p2 == 2):
        print("Player 1 wins")
    elif (p1 == 1 and p2 == 1) or (p1 == 2 and p2 == 2) or (p1 == 3 and p2 == 3):
        print("Match draw")
    elif (p1>3 or p2>3) or (p1<1 or p2<1):
        print("Invalid Move! Please Try Again")
    else:
        print("Player 2 wins\n")


sps()

def reusable():
    print("Want to play again?\n")
    print("1- Yes")
    print("2- No")
    d1 = int(input())
    if d1==1:
        sps()
    elif d1==2:
        print("Thank You")
    else:
        print("Invalid Move")
reusable()
