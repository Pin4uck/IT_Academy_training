def create_password(length, inclusion):
    password = ''
    symbols = ['abcdefghijklmnopqrstuvwxyz']
    if '1' in inclusion:
        symbols.append('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if '2' in inclusion:
        symbols.append('0123456789')
    if '3' in inclusion:
        symbols.append('!@#$%^&_')
    while True:
        for i in symbols:
            password += random.choice(i)
            if len(password) == length:
                break
        if len(password) == length:
            yield ''.join(random.sample(password, len(password)))
            password = ''


def interface():
    num_password = int(input('Enter how many passwords do you want to generate?\n'))
    len_password = int(input('Enter the length of the password. Minimum password length 4 characters\n'))
    while len_password < 4:
        print('Short password. Try again!')
        len_password = int(input('Enter the length of the password. Minimum password length 4 characters\n'))
    add_inclusions = input('Your password will be in lowercase letters.\n'
                           '\n\tIf you want to add capital letters - enter 1,\n'
                           '\tif numbers - enter 2,\n'
                           '\tif special characters, for example "!@#$%^&_" - enter 3.\n'
                           '\nYou can select several, for example "123".\n')
    output = iter(create_password(len_password, add_inclusions))
    count = 0
    while count != num_password:
        print(next(output))
        count += 1


if __name__ == "__main__":
    import random

    not_enough = 'yes'
    while not_enough == 'yes':
        interface()
        not_enough = input('Do you still want to generate a password? Enter "yes" or "no".\n').lower()
    print('Bye!')
