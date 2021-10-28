import random

print('Password Generator')

chars = 'qwertyuiopasdfghjklzxcvbnm' \
        'QWERTYUIOPASDFGHJKLZXCVBNM' \
        '1234567890' \
        '!@#$%^&*()' \
        '-_=+[{]}'";:\|,<.>/?"

amount_of_passwords = input('How many passwords to generate: ')
amount_of_passwords = int(amount_of_passwords)

length_of_password = input('Password length: ')
length_of_password = int(length_of_password)

print('\nGenerated passwords:')

for pwd in range(amount_of_passwords):
    passwords = ''
    for c in range(length_of_password):
        passwords += random.choice(chars)
    print(passwords)