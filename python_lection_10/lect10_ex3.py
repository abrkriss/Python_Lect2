# Задание 3.
#
# Определить, какие из слов «attribute», «класс», «функция», «type»
# невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).
#
# Подсказки:
# --- используйте списки и циклы, не дублируйте функции
# --- обязательно!!! усложните задачу, "отловив" исключение,
# придумайте как это сделать
#

my_list = []
my_list.append("attribute")
my_list.append("функция")
my_list.append("класс")
my_list.append("type")
for el in my_list:
    try:
        s = bytes(el, 'ascii')
        print(type(s), s)
    except UnicodeEncodeError:
        print('Нельзя записать', (type(el), el))
