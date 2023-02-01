# Задание 3. Создать список и заполнить его элементами различных типов данных.
# Реализовать проверку типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
#
# Пример:
# для списка [5, "string", 0.15, True, None]
# результат
#
# <class 'int'>
# <class 'str'>
# <class 'float'>
# <class 'bool'>
# <class 'NoneType'>

list_a = [25, "main", 53.25, None, False]
def my_type(el):
    for el in range(len(list_a)):
        print(type(list_a[el]))
    return
my_type(list_a)

