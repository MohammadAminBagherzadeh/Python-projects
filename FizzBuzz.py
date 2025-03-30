i=0
for i in range(1,101,i+1):
    if i%3==0 and i%5==0:
        print("Fizz Buzz")
        continue
    if i%3==0:
        print("Fizz",end=",")
        continue
    elif i%5==0:
        print("Buzz",end=",")
        continue
    print(i,end=",")