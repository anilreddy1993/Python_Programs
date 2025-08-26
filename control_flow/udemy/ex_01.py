dir = input('Enter the dir: ').strip().lower()

if dir == 'left':
    act = input('Enter the act: ').strip().lower()
    if act == 'wait':
        dr = input('Enter the door color: ').strip().lower()
        if dr == 'yellow':
            print(f'Selected {dr} → You won the game!')
        elif dr == 'red':
            print(f'Selected {dr} → Burned by fire. Game over!')
        elif dr == 'blue':
            print(f'Selected {dr} → Eaten by beasts. Game over!')
        else:
            print(f'Selected {dr} → Wrong door. Game over!')
    else:
        print(f'Selected {act} → Game over!')
else:
    print(f'Selected {dir} → Game over!')