def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

def filter(text):
    result = text.lower()


something = input('Введите текст: ')

if(is_palindrome(something)):
    print('Да, это палиндром')
else:
    print("Нет, это не палиндром")
