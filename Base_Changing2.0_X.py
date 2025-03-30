x=int(input("Enter Number : "))
y=int(input("Enter Base : "))
Sum=0
Sum2=0
Sum8=0
temp=x
while x>0:
    N=x%2
    x//=2
    Sum=Sum*10+N
    if Sum==0:
        Sum=Sum+10+N
while Sum>0:
    M=Sum%10
    Sum//=10
    Sum2=Sum2*10+M
if temp%2==0:
    Sum2//=10
    if y==2:
        print(Sum2)
tem2=Sum2
if y==8:
    while Sum2>=0:
        a=Sum2%1000
        Sum2//=1000
        match a:
            case 0:
                Z=0
            case 1:
                Z=1
            case 10:
                Z=2
            case 11:
                Z=3
            case 100:
                Z=4
            case 101:
                Z=5
            case 110:
                Z=6
            case 111:
                Z=7
        Sum8+=Z
    print(Sum8)