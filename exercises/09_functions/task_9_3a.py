# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):
    try:
        access = dict()
        trunk = dict()
        with open(config_filename, 'r') as config:
            intf = None
            for line in config:
                if not line.strip().startswith('!'):
                    if 'FastEthernet' in line.strip():
                        intf = line.strip().split()[-1]
                    elif 'mode access' in line.strip():
                        access[intf] = 1
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

config = get_int_vlan_map('config_sw2.txt')

for item in config:
    print(item[0])
    if not str(item[1]).isdigit():
        print('VLAN:', ', '.join([str(vlan) for vlan in item[1]]))
    else:
        print('VLAN:', item[1])
