# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

vlans = []

with open('CAM_table.txt', 'r') as _table:
    for line in _table:
        line_split = line.rstrip().split()
        if len(line_split) > 3 and len(line_split[1].split('.')) == 3:
            line_split[0] = int(line_split[0])
            line_split.remove('DYNAMIC')
            vlans.append(line_split)

while True:
    v_number = input('Enter VLAN number: ')
    if v_number.isdigit():
        v_number = int(v_number)
        break
    else:
        print('VLAN был введен не верно!')

for vlan in vlans:
    if v_number == vlan[0]:
        print('{:<4}     {:14}      {:5}'.format(vlan[0], vlan[1], vlan[2]))
