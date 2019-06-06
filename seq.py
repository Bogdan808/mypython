shop_list = ['яблоки', 'манго', 'морковь', 'бананы']
name = 'bogdan'

# Операция индексирования
print('Element 0 :', shop_list[0])
print('Element 1 :', shop_list[1])
print('Element 2 :', shop_list[3])
print('Element 3 :', shop_list[3])
print('Element -1 :', shop_list[-1])
print('Element -2 :', shop_list[-2])

# Вырезка из списка
print('----------------- Вырезка из списка ------------------')
print('Элементы с 1 по 3:', shop_list[1:3])
print('Элементы с 2 до конца:', shop_list[2:])

print('----------------- Вырезка из строки ------------------')
print('Символы с 1 по 3:', name[1:3])
print('Символы с 2 до конца:', name[2:])
print('Символы с 1 до -1:', name[1:-1])
print('Символы от начала до конца:', name[:])

print('------------------ Вырезка с шагом -------------------')
shop_list = ['яблоки', 'манго', 'морковь', 'бананы']
print(shop_list[::1])
print(shop_list[::2])
print(shop_list[::3])
print(shop_list[::-1])



