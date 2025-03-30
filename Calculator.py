Number=int(input("Enter Number : "))
Operand=""
Sum=Number
while not Operand=="=" :
    Operand=str(input("Enter Operand : "))
    if Operand=="=":
        break
    Number=int(input("Enter Number : "))
    match Operand:
        case "+":
            Sum+=Number
        case "-":
            Sum-=Number
        case "*":
            Sum*=Number
        case "/":
            Sum/=Number
print(Sum)

