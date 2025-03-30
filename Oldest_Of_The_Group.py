age=0
max=0
max2=0
while age>=0 :
    age=int(input("Enter age :"))

    if age>=max:
        max=age
    elif age>=max2:
        max2=age
    
    if age>0:
        if age>90 or age<10:
            print("Error")
            break
    else:
        print('maximum age :',max,'   2nd maximum age :',max2)