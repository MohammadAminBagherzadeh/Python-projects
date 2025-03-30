def PrintingTexts (Str) :
    Character=''
    NumberOfCharachters=0
    NumberOfWords=1
    for Ch in Str:
        if Ch==' ':
            Character+='\n'
            NumberOfWords+=1
        else:
            Character+=Ch
            NumberOfCharachters+=1
    return f'{Character}\nNumber of characters :{NumberOfCharachters}\nNumber of words :{NumberOfWords}'

List=[]
Name=str(input("Enter name :"))

while Name!='finish' :
    List.append(Name)
    List.append(' ')
    Name=str(input("Enter name :"))

Str=List

print(PrintingTexts(Str))