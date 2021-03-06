# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_is_true = False
while not ip_is_true:
    ip = input('Введите IP-адрес в формате 10.0.1.1: ')
    ip_split = ip.split('.')
    if len(ip_split) == 4:
        ip_is_true = True
        for ip_split_item in ip_split:
            if not ip_split_item.isdigit():
                ip_is_true = False
                print('IP-адреса введен не верно!\n')
                break
    else:
        print('IP-адреса введен не верно!\n')

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
