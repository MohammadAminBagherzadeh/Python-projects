x = 1
while x>0:
    x=int(input("Enter Number :"))
    for i in range(2,x):
        y=x%i
        if y==0:
            print("False")
            break
    else:
        print("True")