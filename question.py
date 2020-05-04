import random


class Question:
    @property
    def num1(self):
        return self.__num1

    @num1.setter
    def num1(self, value):
        self.__check(value)
        self.__num1 = value
        self.__calculate()

    @property
    def num2(self):
        return self.__num2

    @num2.setter
    def num2(self, value):
        self.__check(value)
        self.__num2 = value
        self.__calculate()

    @property
    def is_plus(self):
        return self.__is_plus

    @is_plus.setter
    def is_plus(self, value):
        self.__is_plus = value
        self.__calculate()

    @property
    def answer(self):
        return self.__answer

    def __calculate(self):
        if self.is_plus:
            self.__answer = self.num1 + self.num2
        else:
            self.__answer = self.num1 - self.num2

    def __get_random_num(self, max, min=0):
        return random.randint(min, max)

    def __check(self, value):
        if value > self.__max:
            raise ValueError

    def __init__(self, max=20):
        self.__max = max
        self.__num1 = self.__get_random_num(self.__max)
        self.__num2 = self.__get_random_num(self.__max)
        self.__is_plus = True if self.__get_random_num(1) == 1 else False
        self.__calculate()

    def __eq__(self, other):
        return True if self.num1 == other.num1 and self.num2 == other.num2 and self.is_plus == other.is_plus else False

    def __str__(self):
        signal = "+" if self.is_plus else "-"
        return str(self.num1) + " " + signal + " " + str(self.num2) + " ="
