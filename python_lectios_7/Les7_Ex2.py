# Задание 2.
#
# Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
# length (длина в метрах), width (ширина в метрах).
#
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
#
# Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
# всего дорожного полотна.
#
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
# метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
# Массу и толщину сделать публичными атрибутами.
# Проверить работу метода.
#
# Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т


class Road:
    _road_mass_sm: float = 0.5

    def __init__(self, length : [float, int], width : [float, int]):
        self._length = float(length)
        self._width = float(width)

    def get_road_mass_sm(self, thickness : float):
        try:
            return(self._width * self._length * self._road_mass_sm * thickness)
        except TypeError:
            return None
if __name__ == '__main__':
    try:
        result = Road(100, 5)
        print("Масса дорожного покрытия", result.get_road_mass_sm(50), "тонн")
    except TypeError:
        print('класс Road требует 2  аргумента')









