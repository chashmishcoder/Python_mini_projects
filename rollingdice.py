import random
import time

print("Hello Welcome to Dice Game...\n")
print("Rules of this game")
print("1. Players have to press ENTER for their turn to be counted")
print("2. The Range of Dice is between 1-6")
print("3. The one who will get two consecutive 6 first will be the winner...\n")
print("-------------------------------------------------------------------------------------------")
print("Game starts now....\n")

while True:
    #player 1 logic
    print("Player 1 : Press ENTER for your move")
    p1 = input()
    r1 = random.randint(1,6)
    print("Please wait.. Dice is Rolling...")
    time.sleep(3)
    print("Player 1 got:",r1,"\n")

    if r1==6:
        print("You got : 6.... Repeat your turn\n")
        print("Player 1 : Press ENTER for your move")
        p = input()
        r = random.randint(1, 6)
        print("Please wait.. Dice is Rolling...")
        time.sleep(3)
        print("Player 1 got:", r, "\n")
        if r==6:
            print("-----------------------------------------------")
            print("Congratulations! Player 1 Wins\n")
            print("Game Ends....")
            break


    #Player 2 logic
    print("Player 2 : Press ENTER for your  move")
    p2 = input()
    r2 = random.randint(1,6)
    print("Please wait.. Dice is Rolling...")
    time.sleep(3)
    print("Player 2 got:",r2,"\n")


    if r2==6:
        print("You got : 6.... Repeat your turn\n")
        print("Player 2 : Press ENTER for your  move")
        q = input()
        w = random.randint(1, 6)
        print("Please wait.. Dice is Rolling...")
        time.sleep(3)
        print("Player 2 got:", w, "\n")
        if w==6:
            print("-----------------------------------------------")
            print("Congratulations! Player 2 Wins\n")
            print("Game Ends....")
            break

