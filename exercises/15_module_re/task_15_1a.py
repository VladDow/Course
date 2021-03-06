# -*- coding: utf-8 -*-
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом,
чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""

import re
from pprint import pprint


def get_ip_from_cfg(file_config):
    config_ip = {}
    with open(file_config, 'r') as config:
        for line in config:
            if line.startswith('interface'):
                regular = re.compile(r'\S+ (\S+)')
                key = regular.search(line).group(1)
            if line.startswith(' ip address'):
                regular = re.compile(r' ip address (?P<ip>\S+) (?P<mask>\S+)')
                config_ip[key] = regular.search(line).groups()
    return config_ip


if __name__ == '__main__':
    pprint(get_ip_from_cfg('config_r1.txt'))
