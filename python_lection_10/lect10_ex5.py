"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""


import subprocess
import chardet
import os

ping_res_1 = ['ping', 'yandex.ru']
ping_res_2 = ['ping', 'youtube.com']
ya_ping_1 = subprocess.Popen(ping_res_1, stdout=subprocess.PIPE)
ya_ping_2 = subprocess.Popen(ping_res_2, stdout=subprocess.PIPE)
print(ya_ping_1.stdout)
print(ya_ping_2.stdout)
for line in ya_ping_1.stdout:
    result = chardet.detect(line)
    print(line.decode(result['encoding']))
for line in ya_ping_2.stdout:
    result = chardet.detect(line)
    print(line.decode(result['encoding']))

