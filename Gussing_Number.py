import random

def Gusse(n,k):
    x=random.randint(n,k)
    print(x)
    c=str(input("High(h) or Low(l) or Same(s) ?"))
    if c=="h":
        n=(x+1)
        return Gusse(n,k)
    elif c=="l":
        k=(x-1)
        return Gusse(n,k)
    elif c=="s":
        return f'\n Your number is : {x}'

n=1
k=99

print(Gusse(n,k))