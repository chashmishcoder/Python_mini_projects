
print("Enter a number")
num = input()
prev = num[0]

i =1
while i<=len(num)-1:
    if num[i]==prev:

        print("Yes")
        break
    else:
        prev = num[i]

        i=i+1
if i>len(num)-1:
 print("no")

