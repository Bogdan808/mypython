def printMax(x,y):
    '''Hello my comment'''

    x = int(x)
    y = int(y)
    if x > y:
        print(x, 'большее')
    else:
        print(y, 'большее')
printMax(2,4)
print(printMax.__doc__)