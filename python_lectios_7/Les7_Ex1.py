# Задание 1.
#
# Создать класс TrafficLight (светофор)
# и определить у него один приватный атрибут color (цвет) и публичный метод
# running (запуск).
#
# В рамках метода running реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный)
# составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
# на ваше усмотрение.
# Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
#
# Переключение между режимами должно осуществляться только
# в указанном порядке (красный, желтый, зеленый).
#
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# """
import time


class TrafficLight:
    color_time = {'red': 7,
                  'yellow': 2,
                  'green': 5}
    __color = None
    __color_index = 0
    color_count = 3

    def __init__(self, init_color='red', color_count=3):
        self.__color = init_color if self.color_time.get(init_color) \
            else list(self.color_time.keys())[self.__color_index]
        self.__color_index = list(self.color_time.keys()).index(self.__color)
        self.color_count = color_count

    def running(self):
        print(self.__color)
        while self.color_count:
            time.sleep(self.color_time.get(self.__color))
            self.__color_index = (self.__color_index + 1) % 3
            self.__color = list(self.color_time.keys())[self.__color_index]
            print(self.__color)
            self.color_count -= 1

if __name__ == '__main__':
    while True:
        color_count = input("Сколько раз сменить цвета? ")
        try:
            color_count = int(color_count)
            break
        except ValueError as e:
            print('Нужно целое число')
    lights = TrafficLight('red', color_count)
    lights.running()
