import random
s = ""
s1 = ""
i = 1
while i<=5:
    a=random.randint(65,90)
    b = chr(a)
    s = s + b

    c = a + 1
    if c>90:
        c= 65
    d = chr(c)
    s1 = s1 + d
    i=i+1
print(s,"- ",end="")
print(s1)