List=[]
Age=1
max=0
max2nd=0

while Age>0 :
    Age=int(input('Enter Age :'))
    
    if Age>90 or Age<10 :
        print('Error')
    else :
        List.append(Age)

for member in List :
    
    if member>max :
        max2nd=max
        max=member
    elif member>max2nd :
        max2nd=member
    
print(f"Max= {max}    2ndMax= {max2nd}")