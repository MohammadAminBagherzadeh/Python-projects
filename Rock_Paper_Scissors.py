import random

z=str(input('Enter Rock,Paper or Scissors :'))
y=random.randint(1,3)

match y :
    case 1:
        y='Rock'
    case 2:
        y='Paper'
    case 3:
        y='Scissors'

while z=='Rock' :
    match y :
        case 'Rock':
            print('Draw')
            print('Rock')
        case 'Paper':
            print('CPU Won')
            print('Paper')
        case 'Scissors':
            print('YOU Won')
            print('Scissors')
    break
while z=='Paper' :
    match y :
        case 'Rock':
            print('YOU Won')
            print('Rock')
        case 'Paper':
            print('Draw')
            print('Paper')
        case 'Scissors':
            print('CPU Won')
            print('Scissors')
    break
while z=='Scissors' :
    match y :
        case 'Rock':
            print('CPU Won')
            print('Rock')
        case 'Paper':
            print('YOU Won')
            print('Paper')
        case 'Scissors':
            print('Draw')
            print('Scissors')
    break