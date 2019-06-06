x = 50

def func():
    global x

    print('x =', x)

    x = 2
    print('Заменяем глобальное значение x на', x)

func()

print('Зачение x составляет', x)
