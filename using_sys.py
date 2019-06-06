from sys import argv

print('Аргументы командной строки:')

#
# for i in sys.argv:
#     print(i)
#

if argv[1] == 'bogdan':
    print('Hello Bogdan')
else:
    print('You are not Bogdan')

# print('\n\nПеременная PYTHONPATH содержит', path, '\n')
