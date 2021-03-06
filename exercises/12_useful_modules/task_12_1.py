# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

import subprocess


def ping_ip_addresses(ip_list):
    ip_list_work = []
    ip_list_not = []
    for ip in ip_list:
        results = subprocess.run(['ping', '-c', '3', '-n', ip])
        if results.returncode == 0:
            ip_list_work.append(ip)
        else:
            ip_list_not.append(ip)
    return (ip_list_work, ip_list_not)

