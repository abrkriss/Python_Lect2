# """
# 2. Задание на закрепление знаний по модулю json. Есть файл orders
# в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
# его заполнение данными.
#
# Для этого:
# Создать функцию write_order_to_json(), в которую передается
# 5 параметров — товар (item), количество (quantity), цена (price),
# покупатель (buyer), дата (date). Функция должна предусматривать запись
# данных в виде словаря в файл orders.json. При записи данных указать
# величину отступа в 4 пробельных символа;
# Проверить работу программы через вызов функции write_order_to_json()
# с передачей в нее значений каждого параметра.
#
# ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
# ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ
#
# {
#     "orders": []
# }
#
# вам нужно подгрузить JSON-объект
# и достучаться до списка, который и нужно пополнять
# а потом сохранять все в файл
# """

import json
from datetime import datetime


def  write_order_to_json():
    dict_to_json = {'orders':[{'item': input('Введите товар '), 'quantity' : int(input('Введите количество ')),
                    'price': int(input('Введите цену ')),
                    'buyer': input('Введите покупателя '), 'data': input('Введите дату(дд.мм.гггг) ')}]}
    return dict_to_json


def write():
    dict_to_json = write_order_to_json()
    with open("res.json", 'w', encoding='utf-8') as my_f:
        json.dump(dict_to_json, my_f, indent=4, separators=(',', ': '))

    with open("res.json")as my_f:
        print(my_f.read())


write()