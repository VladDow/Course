# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):
    try:
        access = dict()
        trunk = dict()
        with open(config_filename, 'r') as config:
            for line in config:
                if not line.strip().startswith('!'):
                    if 'FastEthernet' in line.strip():
                        intf = line.strip().split()[-1]
                    elif 'access vlan' in line.strip():
                        access[intf] = int(line.strip().split()[-1])
                    elif 'trunk allowed vlan' in line.strip():
                        trunk[intf] = [int(item) for item in line.strip().split()[-1].split(',')]
        results = access
        results.update(trunk)
        return tuple(results.items())
    except FileNotFoundError:
        print('Ошибка в имени файла!')
        return None

config = get_int_vlan_map('config_sw1.txt')

for item in config:
    print(item[0])
    if not str(item[1]).isdigit():
        print('VLAN:', ', '.join([str(vlan) for vlan in item[1]]))
    else:
        print('VLAN:', item[1])
