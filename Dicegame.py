import random
import time
i=1
while i<=1000:
    print("\nUser Turn :")
    print("Enter any Number Between : 1-6")
    num = int(input())

    if num > 6:
        print("\nInvalid Choice, Please Enter Correctly")
    elif num<=6:

        print("\nComputer Turn")
        print("Computer will play its turn")
        print("PLease wait...")
        time.sleep(2)
        a = random.randint(1,6)
        print(a)

        if num!=a:
            i = i+1
        else:
            print("Computer wins")
            break
