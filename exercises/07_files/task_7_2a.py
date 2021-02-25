# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

import sys

try:
    with open(sys.argv[1], 'r') as config:
        for line in config:
            flag = True
            if not line.startswith('!'):
                for ignore_word in ignore:
                    if line.strip().count(ignore_word.strip()) != 0:
                        flag = False
                        break
                if flag:
                    print(line.rstrip())
except IndexError or FileNotFoundError:
    print('Имя файла, вероятно, введено не корректно!')
