import random


def generate_password(length: int, pass_chars: str):
    password = random.sample(pass_chars, length)
    return ''.join(password)


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

count_passwords = int(input('Сколько паролей вы хотите?: '))
len_password = int(input('Введите длину пароля: '))

answer = input('Содержит цифры 0 - 9? [д/н]: ')
if answer == 'д':
    chars += digits

answer = input('Содержит буквы в нижнем регистре? [д/н]: ')
if answer == 'д':
    chars += lowercase_letters

answer = input('Содержит буквы в верхнем регистре? [д/н]: ')
if answer == 'д':
    chars += uppercase_letters

answer = input('Содержит символы "!#$%&*+-=?@^_"? [д/н]: ')
if answer == 'д':
    chars += punctuation

answer = input('Исключать ли неоднозначные символы "il1Lo0O"? [д/н]: ')
if answer == 'д':
    for char in 'il1Lo0O':
        chars = chars.replace(char, '')

for _ in range(count_passwords):
    print(generate_password(len_password, chars))
