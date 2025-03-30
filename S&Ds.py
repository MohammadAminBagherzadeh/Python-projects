Dict={}
Sum=0
Subject=str(input("Enter Subject :"))

while Subject!="=" :
    Grade=float(input("Enter Grade :"))
    Dict[Subject]=Grade
    Sum+=Grade
    Subject=str(input("Enter Subject :"))

for key in Dict :
    print(key," :",Dict[key])

print("Avg :",Sum/len(Dict))
