zoo = ('python', 'elephant', 'penguin')
print('Количество животных в зоопарке -', len(zoo))

new_zoo = 'monkey', 'camel', zoo

print('Количество клеток в зоопарке -', len(new_zoo))
print('Все животные в новом зоопарке:', new_zoo)
print('Животные, привезённые из старого зоопарка:', new_zoo[2])
print('Последнее животное, привезённое из старого зоопарка -', new_zoo[2][2])
print('Количество животных в новом зоопарке -', len(new_zoo)-1+len(new_zoo[2]))