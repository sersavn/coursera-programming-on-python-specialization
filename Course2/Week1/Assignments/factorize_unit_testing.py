'''
Дана функция factorize(x) со следующим контрактом:
def factorize(x):
    """ Factorize positive integer and return its factors.
        :type x: int,>=0
        :rtype: tuple[N],N>0
    """
    pass

Написать комплект тестов:

test_wrong_types_raise_exception
test_negative
test_zero_and_one_cases
test_simple_numbers
test_two_simple_multipliers
test_many_multipliers
Проверить в них соответственно:

Что типы float и str (значения 'string', 1.5) вызывают исключение TypeError.
Что для отрицательных чисел -1, -10 и -100 вызывается исключение ValueError.
Что для числа 0 возвращается кортеж (0,), а для числа 1 кортеж (1,)
Что для простых чисел 3, 13, 29 возвращается кортеж, содержащий одно данное число.
Что для чисел 6, 26, 121 возвращаются соответственно кортежи (2, 3), (2, 13) и (11, 11).
Что для чисел 1001 и 9699690 возвращаются соответственно кортежи (7, 11, 13) и (2, 3, 5, 7, 11, 13, 17, 19).
При этом несколько различных проверок в рамках одного теста должны быть обработаны как подслучаи с указанием x: subTest(x=...).

ВАЖНО! Название переменной в тестовом случае должно быть именно "x".
Все входные данные должны быть такими, как указано в условии.
В задании необходимо реализовать ТОЛЬКО класс TestFactorize, кроме этого реализовывать ничего не нужно.
Импортировать unittest и вызывать unittest.main() в решении также не нужно.
'''


def factorize(x):
    """ Factorize positive integer and return its factors.
        :type x: int,>=0
        :rtype: tuple[N],N>0
    """
    pass


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        cases = ['string', 1.5]
        for i in cases:
            with self.subTest(x = i):
                self.assertRaises(TypeError, factorize, i)

    def test_negative(self):
        cases = [-1, -10, -100]
        for i in cases:
            with self.subTest(x = i):
                self.assertRaises(ValueError, factorize, i)

    def test_zero_and_one_cases(self):
        cases = [0, 1]
        for i in cases:
            with self.subTest(x = i):
                self.assertTupleEqual(factorize(i), (i, ))

    def test_simple_numbers(self):
        cases = [3, 13, 29]
        for i in cases:
            with self.subTest(x = i):
                self.assertTupleEqual(factorize(i), (i, ))

    def test_two_simple_multipliers(self):
        cases = [6, 26, 121]
        output = [(2,3), (2, 13), (11, 11)]
        for num, val in enumerate(cases):
            with self.subTest(x = val):
                self.assertTupleEqual(factorize(val), output[num])

    def test_many_multipliers(self):
        cases = [1001, 9699690]
        output = [(7, 11, 13), (2, 3, 5, 7, 11, 13, 17, 19)]
        for num, val in enumerate(cases):
            with self.subTest(x = val):
                self.assertTupleEqual(factorize(val), output[num])
