from random import randint
import os

def is_valid(string):
    if string.isdigit():
        if 1 <= int(string) <= 100:
            return True
    return False


print('Добро пожаловать в игру "Угадай число"')

answer = 'д'
while answer == 'д':
    num = randint(1, 100)
    print('Я загадал число от 1 до 100. Попробуй угадать его.')
    flag = True
    cnt = 1

    while flag:
        user_num = input(f'Попытка {cnt}. Введите число от 1 до 100: ')
        if is_valid(user_num):
            user_num = int(user_num)
            if user_num > num:
                print('Мое число меньше')
                cnt += 1
            elif user_num < num:
                print('Мое число больше')
                cnt += 1
            else:
                print('Угадали!!!')
                flag = False
        else:
            print('Нет, нужно целое число от 1 до 100')

    answer = input('Сыграем еще раз? да - д, нет - н: ')
    os.system('cls')

print('Спасибо за игру!')
input('Для выхода нажмите Enter')





