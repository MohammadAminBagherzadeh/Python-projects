num=0
Sum=0
X=int(input("How many calculations?: "))
if X >=0:
    for num in range(X):
        Number=int(input("Enter Number: "))
        Sum+=Number
    print(Sum)
else:
    print("Error")