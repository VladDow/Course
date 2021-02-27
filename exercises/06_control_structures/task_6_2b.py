# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_is_true = False
while not ip_is_true:
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
