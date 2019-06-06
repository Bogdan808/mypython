def reverse(text):
    return text[::-1]

def is_polidrom(text):
    return text == reverse(text)

def filter(text):
    forbidden = ('.', '?', '!', ':', ';', '-', '—', '(', ')', '[', ']', '...', '’', '“', '”', '/', ',')
    newtext = [x for x in text if not x in forbidden]
    newtext = ''.join(newtext)

    return newtext

usertext = input('Input text please:')
# usertext = 'Poop ana poop?'
usertext = usertext.lower()
usertext = filter(usertext)

if is_polidrom(usertext):
    print('Yes, {0} is a polidrome'.format(usertext))
else:
    print('No, {0} is not a polidrome'.format(usertext))
