# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_is_true = False

ip = input('Введите IP-адрес в формате 10.0.1.1: ')
ip_split = ip.split('.')
if len(ip_split) == 4:
    ip_is_true = True
    for ip_split_item in ip_split:
        if not ip_split_item.isdigit() or int(ip_split_item) < 0 or int(ip_split_item) > 255:
            ip_is_true = False
            print('Неправильный IP-адрес')
            break
else:
    print('Неправильный IP-адрес')

if ip_is_true:
    oct1 = int(ip.split('.')[0])
    if oct1 <= 223 and oct1 >= 1:
        print('unicast')
    elif oct1 <= 239 and oct1 >= 224:
        print('multicast')
    elif ip.strip() == '255.255.255.255':
        print('local broadcast')
    elif ip.strip() == '0.0.0.0':
        print('unassigned')
    else:
        print('unused')
