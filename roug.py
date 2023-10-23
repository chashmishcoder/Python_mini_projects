
print("Enter a number")
num = input()
prev = num[0]
count = 0
i =1
while i<=len(num)-1:
    if num[i]==prev:
        count+=1


    else:
        prev = num[i]
        count=0
    i=i+1
if i>len(num)-1:
 print("no")

