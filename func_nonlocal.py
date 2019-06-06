def func_outer():
    x = '2'
    print('x равно', x)

    def func_inner():
        # nonlocal x
        x += '5'

    func_inner()
    print('Локальное x сменилось на', x)

func_outer()

#
# def user():
#     name = 'Bogdan'
#
#     def addLastName(lastname):
#         nonlocal name
#         name += lastname
#
#     addLastName(' Nasikovsky')
#
#     print(name)
#
#
# user()