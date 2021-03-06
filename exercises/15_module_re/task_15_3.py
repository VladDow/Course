# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT
из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""

import re


def convert_ios_nat_to_asa(name_file_config, file_config):
    with open(name_file_config, 'r') as file_config_r, open(file_config, 'w') as file_config_w:
        for line in file_config_r:
            regular = re.compile(r'ip (?P<type_nat>\S+) \S+ \S+ (?P<type_s>\S+) (?P<type_net>\S+) (?P<ip>\S+) (?P<ip_n>\S+) \S+ \S+ (?P<intf_n>\S+)', )
            result = regular.search(line)
            template = 'object network LOCAL_{}\n host {}\n {} (inside,outside) {} interface service {} {} {}\n'
            file_config_w.write(template.format(result.group('ip'), result.group('ip'), result.group('type_nat'), result.group('type_s'),
                                result.group('type_net'), result.group('ip_n'), result.group('intf_n')))


if __name__ == '__main__':
    convert_ios_nat_to_asa('cisco_nat_config.txt', 'test.txt')
