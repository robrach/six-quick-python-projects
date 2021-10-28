import random


def password_generator(amount_of_passwords, length_of_password):
    amount_of_passwords = int(amount_of_passwords)
    length_of_password = int(length_of_password)

    chars = 'qwertyuiopasdfghjklzxcvbnm' \
        'QWERTYUIOPASDFGHJKLZXCVBNM' \
        '1234567890' \
        '!@#$%^&*()' \
        '-_=+[{]}'";:\|,<.>/?"

    print('\nGenerated passwords:')

    for password_being_generated in range(amount_of_passwords):
        password = ''
        for position in range(length_of_password):
                password += random.choice(chars)
        print(password)


if __name__ == '__main__':
    print('Password Generator')
    amount_of_passwords = input('How many passwords to generate: ')
    length_of_password = input('Password length: ')
    password_generator(amount_of_passwords, length_of_password)