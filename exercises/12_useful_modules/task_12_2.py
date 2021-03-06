# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""

import ipaddress


def check_ip(ip):
    try:
        ipaddress.ip_network(ip)
        return True
    except ValueError:
        return False


def convert_ranges_to_ip_list(convert_ip_list):
    ip_list = []
    for ip in convert_ip_list:
        if not check_ip(ip):
            if ip.split('.')[-1].find('-') != -1:
                ip_split = ip.split('.')
                ip_split_range = [int(ip) for ip in ip_split[-1].split('-')]
                for num in range(ip_split_range[0], ip_split_range[1] + 1):
                    ip_list.append( '.'.join(ip_split[:3]) + '.' + str(num))
            else:
                ip_split = ip.split('-')
                ip_start = int(ip_split[0].split('.')[-1])
                ip_end = int(ip_split[1].split('.')[-1])
                for num in range(ip_start, ip_end + 1):
                    ip_list.append( '.'.join(ip_split[0].split('.')[:3]) + '.' + str(num))
        else:
            ip_list.append(ip)
    return ip_list


if __name__ == '__main__':
    test = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
    print(convert_ranges_to_ip_list(test))
