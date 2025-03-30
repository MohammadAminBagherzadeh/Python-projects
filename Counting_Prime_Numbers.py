x=int(input("Enter Number : "))
sum=0
for i in range(3,x+1):
    for j in range(2,i):
        y=i%j
        if y==0:
            break
    else:
        sum+=1
print(sum)