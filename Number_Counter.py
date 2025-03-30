n=int(input('Enter Number :'))
Sum=0
if n<0:
    n*=-1
while n>0:
    n//=10
    Sum+=1
print(Sum)