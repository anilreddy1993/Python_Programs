#password testing programs

pd = input('Enter the password: ')

if len(pd) >= 8:
    print('Length matched')

    if any(ch.isalpha() for ch in pd):
        print('Contains letters')

        if any(ch.isdigit() for ch in pd):
            print('Contains numbers')

            if any(not ch.isalnum() for ch in pd):  # Special character check
                print('Contains special characters')
                print('Password is valid')
            else:
                print('Password must contain at least one special character')
        else:
            print('Password must contain at least one digit')
    else:
        print('Password must contain at least one letter')
else:
    print('Length not matched')
























