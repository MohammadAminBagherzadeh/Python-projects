Day=int(input('enter day: ')) 
Month=int(input('enter month: '))
if Month<=6 and Month>=1 and Day<=31 :
    DayOfTheYear=(Month-1)*31+Day
    print(DayOfTheYear)
elif Month>6 and Month<=12 and Day<=30 :
    month=(Month-1)*30
    DayOfTheYear=month+6+Day
    print(DayOfTheYear)
else :
    print("ERROR")   