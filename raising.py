class ShortInputExeption(Exception):
    '''Пользовательский класс исключения'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = input('Write please:')
    if len(text) < 3:
        raise ShortInputExeption(len(text), 3)
except EOFError:
    print('Ну зачем вы сделали мне EOF?')
except ShortInputExeption as ex:
    print('ShortInputException: Длина введённой строки -- {0}; ожидалось, как минимум, {1}'.format(ex.length, ex.atleast))
else:
    print('Не было исключений.')