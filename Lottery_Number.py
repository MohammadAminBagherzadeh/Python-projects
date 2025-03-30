import random
for j in range(100) :
    number=random.randint(1,9999)
    Len=len(str(number))
    x=4-Len
    print(x*'0',end='')
    print(number)
