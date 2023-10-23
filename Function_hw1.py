def code():
    print("Enter a number")
    a = int(input())
    bi = bin(a)
    hx = hex(a)
    ot = oct(a)
    print("Binary value of",a,"is :",bi)
    print("Hexa-Decimal value of", a, "is :", hx)
    print("Octal value of", a, "is :", ot)

print("Program starts here...")
code()
print("\nSecond Time...")
code()
