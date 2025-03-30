points=0
wins=0
draws=0
loses=0
for i in range(30) :
    point=int(input('point : '))
    points=point+points
    if point==0 :
        loses+=1
    elif point==1 :
        draws+=1
    elif point==3 :
        wins+=1
print('wins:',wins,'    draws:',draws,'    loses:',loses,'    total points:',points)