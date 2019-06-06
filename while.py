number = 23
running = True

while running:
    guess = int(input('Input your number : '))

    if guess == number:
        print('You victory')
        running = False
    elif guess < number:
        print('No, the unknown number a little more than that')
    else:
        print('No, the unknown number a little less.')

else:
    print('Loop while finished!')

print('Finished programm')
