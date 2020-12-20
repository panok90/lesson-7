"""Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""


from abc import ABC, abstractmethod


class Clothes(ABC):
    _consumption = 0

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def material_consumption(self):
        pass

    @classmethod
    def display_on(cls):
        return f'Расход материала: {cls._consumption}'


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def material_consumption(self):
        self.consumption_in_coat = round(self.size / 6.5 + 0.5, 2)
        Clothes._consumption = Clothes._consumption + self.consumption_in_coat

    @property
    def get_consumption(self):
        print(f'Расход на {self.name} составил: {self.consumption_in_coat}')


class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    def material_consumption(self):
        self.consumption_in_suit = round(2 * self.height + 0.3, 2)
        Clothes._consumption = Clothes._consumption + self.consumption_in_suit

    @property
    def get_consumption(self):
        print(f'Расход на {self.name} составил: {self.consumption_in_suit}')


coat_1 = Coat("Лама", 50)
coat_1.material_consumption()
coat_1.get_consumption
coat_2 = Coat("Альпака", 54)
coat_2.material_consumption()
coat_2.get_consumption
suit_1 = Suit("Двойка", 1.85)
suit_1.material_consumption()
suit_1.get_consumption
suit_2 = Suit("Тройка", 2.04)
suit_2.material_consumption()
suit_2.get_consumption
print(Clothes.display_on())
