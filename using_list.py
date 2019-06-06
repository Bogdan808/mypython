
shop_list = ['apple', 'mango', 'carrot', 'banana']

print('Я должен сделать', len(shop_list), 'покупки.')

print('Покупки:', end=' ')

for item in shop_list:
    print(item, end=' ,')

print('\nТакже нужно купить риса.')

print('Отсортирую-ка я свой список')

shop_list.sort()
print('Отсортированный список покупок выглядит так:', shop_list)

print('Первое, что мне нужно купить, это', shop_list[0])

olditem = shop_list[0]

del shop_list[0]

print('Я купил', olditem)

print('Теперь мой список покупок:', shop_list)
