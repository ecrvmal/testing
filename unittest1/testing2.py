import unittest
from art import tprint


def my_summ(a,b):
    return a + b


class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name

class TestSuit(unittest.TestCase):
    def setUp(self):
        self.pers1 = Person('Ivan', 23)

    def tearDown(self):
        pass

    def test_number1(self):
        self.assertEqual(my_summ(3, 5), 8)

    def test_number2(self):
        self.assertTrue(isinstance(my_summ(3, 5), int))

    def test_number3(self):
        self.assertFalse(isinstance(my_summ(3, 5), list))

    def test_number4(self):
        self.assertLess(my_summ(3, 5), 10)

    def test_number5(self):
        self.assertAlmostEqual(my_summ(3, 5.00000001), 8)

    def test_pers1(self):
        self.assertNotEqual(self.pers1.name, 'Iva', "test_pers1 failed")


if __name__ == '__main__':
    tprint('Starting   Unittest')
    unittest.main()
