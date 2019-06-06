while True:
    s = input( 'Please write something :' )
    if len(s) < 3:
        print('Too little')
        continue
    print('The input string is of sufficient length')