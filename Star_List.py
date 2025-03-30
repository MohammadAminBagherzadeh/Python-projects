List=[]
List1=[]
Number=0

while Number>=0 :
    Number=int(input("Enter Number :"))
    List.append(Number)


for Number in List :
    
    if Number>0:
        List1.append(Number*'*')

print(List1)