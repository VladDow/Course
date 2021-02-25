# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

with open('ospf.txt') as ospf:
    for line in ospf:
        line_split = line.split()
        print('''Prefix                {:20}\nAD/Metric             {:20}\nNext-Hop              {:20}\nLast update           {:20}\nOutbound Interface    {:20}\n'''.format(line_split[1], line_split[2].strip('[]'), line_split[4].strip(','), line_split[5].strip(','), line_split[6]))
