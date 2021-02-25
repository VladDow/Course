# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

import sys

try:
    with open(sys.argv[1], 'r') as config, open(sys.argv[2], 'w') as _config:
        for line in config:
            flag = True
            if not line.startswith('!'):
                for ignore_word in ignore:
                    if line.strip().count(ignore_word.strip()) != 0:
                        flag = False
                        break
                if flag:
                    _config.write(line.rstrip() + '\n')
except IndexError or FileNotFoundError:
    print('Имя файла, вероятно, введено не корректно!')
