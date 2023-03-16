
class NonNegative:

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    wage = NonNegative()
    bonus = NonNegative()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus


class Position(Worker):

    @property
    def get_full_name(self):
        return self.name + " " + self.surname + " " + self.position

    @property
    def get_total_income(self):
        return self.wage + self.bonus


OBJ = Position('Иван', 'Иванов', 'Manager', 10, 100)
print(OBJ.get_full_name)
print(OBJ.get_total_income)
