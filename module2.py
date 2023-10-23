import module1
print("Enter two values")
val1 = int(input())
val2 = int(input())

print("\nEnter your choice")
print("1- Addition")
print("2- Subtraction")
print("3- Multiplication")
print("4- Division")
print("5- Power")

uchoice = int(input())

if uchoice==1:
    module1.addition(val1,val2)
elif uchoice==2:
    module1.subtraction(val1,val2)
elif uchoice==3:
    module1.multiplication(val1,val2)
elif uchoice==4:
    module1.division(val1,val2)
else:
    module1.power(val1,val2)

