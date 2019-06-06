poem = '''\
Programming is fun.
If work is boring,
To give her a cheerful tone -
use python!
'''

f = open('poem.txt', 'a')
f.write(poem)
f.close()


f = open('poem.txt')

while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end='')

f.close()