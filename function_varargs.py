def total(a=5, *numbers, **phonebook):
    print('a',a)

    for item in numbers:
        print('item: ', item)

    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


total(10,1,2,3,Jack=1123,John=2231,Inge=1560)