x=int(input("Enter Width :"))
y=int(input("Enter Height :"))
for j in range(1,y+1):
    if j==1 or j==y:
        for i in range(1,x+1):
            print("*  ",end='')
        print()   
    else : 
        print("*  ",end='')
        for ii in range(1,x-1):
            print("   ",end='')
        print("*  ")