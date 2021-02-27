# -*- coding: utf-8 -*-
"""
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
- ключи: имена интерфейсов, вида 'FastEthernet0/1'
- значения: список команд, который надо
  выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

def generate_trunk_config(intf_vlan_mapping, trunk_template):
    '''
    Параметры функции:
    intf_vlan_mapping: ожидает как аргумент словарь с соответствием интерфейс-VLANы
    такого вида:
        {'FastEthernet0/1': [10, 20],
        'FastEthernet0/2': [11, 30],
        'FastEthernet0/4': [17]}
    
    trunk_template: ожидает как аргумент шаблон конфигурации trunk-портов в виде
    списка команд (список trunk_mode_template)

    Функция возвращает список команд с конфигурацией на основе указанных портов
    и шаблона trunk_mode_template.
    '''
    results = dict()
    for intf, vlan in intf_vlan_mapping.items():
        results[intf] = list()
        for line in trunk_template:
            if line.strip().endswith('vlan'):
                results[intf].append('{command} {vlans}'.format(command = line.strip(), vlans = ','.join([str(vl) for vl in vlan])))
            else:
                results[intf].append(line)
    return results

template = generate_trunk_config(trunk_config, trunk_mode_template)

for intf, command in template.items():
    print('interface {}\n'.format(intf),'\n'.join(command))
