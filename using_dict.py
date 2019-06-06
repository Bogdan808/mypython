ab = {
    'Swaroop': 'swaroop@swaroop.com',
    'Larry': 'larry@mail.ru',
    'Matsumoto': 'matsumoto@mail.ru',
    'Spammer': 'spammer@mail.ru'
}

print('Swaroop`s address:', ab['Swaroop'])

del ab['Spammer']

print('\nВ адресной книге {0} контакта\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {0} have address: {1}'.format(name, address))

ab['Bogdan'] = 'bogdan808@ya.ru'

if 'Bogdan' in ab:
    print('\nAddress of Bogdan:', ab['Bogdan'])
