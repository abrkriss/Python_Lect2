# Задание 4.
#
# Преобразовать слова «разработка», «администрирование», «protocol»,
# «standard» из строкового представления в байтовое и выполнить
# обратное преобразование (используя методы encode и decode).
#
# Подсказки:
# --- используйте списки и циклы, не дублируйте функции

my_list = []
my_list.append("разработка")
my_list.append("администрирование")
my_list.append("protocol")
my_list.append("standard")


def coding(my_list):
    count = 1
    for el in my_list:
        my_list_bytes = str.encode(el, encoding='utf-8')
        print(count, my_list_bytes)
        print(type(my_list_bytes))
        my_list_s = bytes.decode(my_list_bytes, encoding='utf-8')
        print(count, my_list_s)
        print(type(my_list_s))
        count += 1



coding(my_list)


