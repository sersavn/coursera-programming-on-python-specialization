#my solution of the assignment

'''
В этом задании вам даны 3 класса A, B, C, имеющие сходный (но не одинаковый) интерфейс.
Вам необходимо создать абстрактный базовый класс Base и построить корректную схему наследования.
При выполнении следует избегать дублирования кода, и стараться следовать SOLID принципам ООП.
Кроме того, рекомендуется самостоятельно тестировать код перед отправкой, а также при написании следовать стандарту PEP 8.
'''

'''
In the current task you have 3 classes with similar interface.
Create an abstract base class Base and build an correct inheretance schema.
Avoid duplicates and try to follow SOLID princeples of OOP.
It is recommended to manually test code before submitting solution and follow PEP 8 standart.
'''

import math
from abc import ABC, abstractmethod

class Base(ABC):
    '''
    variable 'data' takes list of float elements
    each element lay in range (0.0, 1.0)

    variable 'result' takes list of integer elements
    each element lay in range [0, 1]

    len(result) == len(data)
    '''
    def __init__(self, data, result):
        self.data = data
        self.result = result

    '''
    @abstractmethod нужно было использовать по заданию
    '''
    @abstractmethod
    def get_answer(self):
        return [int(x >= 0.5) for x in self.data]

    def get_score(self):
          ans = self.get_answer()
          return sum([int(x == y) for (x, y) in zip(ans, self.result)]) \
              / len(ans)

    def get_loss(self):
        return sum([(x - y) * (x - y) for (x, y) in zip(self.data,
                   self.result)])

class A(Base):

    def get_answer(self):
        return [int(x >= 0.5) for x in self.data]


class B(Base):

    def get_answer(self):
        return [int(x >= 0.5) for x in self.data]

    def get_loss(self):
        return -sum([y * math.log(x) + (1 - y) * math.log(1 - x)
                    for (x, y) in zip(self.data, self.result)])

    def calc_res(self):
        ans = self.get_answer()
        res = [int(x == 1 and y == 1) for (x, y) in zip(ans,
               self.result)]
        return res

    def get_pre(self):
        ans = self.get_answer()
        res = self.calc_res()
        return sum(res) / sum(ans)

    def get_rec(self):
        res = self.calc_res()
        return sum(res) / sum(self.result)

    def get_score(self):
        pre = self.get_pre()
        rec = self.get_rec()
        return 2 * pre * rec / (pre + rec)


class C(Base):

    def get_answer(self):
        return [int(x >= 0.5) for x in self.data]

    def get_loss(self):
        return sum([abs(x - y) for (x, y) in zip(self.data,
                   self.result)])
