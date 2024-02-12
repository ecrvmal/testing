import unittest
from sum import sum_squares, split

class TestSumKV(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(sum_squares(2, 3), 13)


class SplitTesting(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_simplestring(self):
        result = split('My_work 20 100.500')
        self.assertEqual(result, ['My_work', '20', '100.500'])

    def test_type_change(self):
        result = split('My_work 20 100.500', [str, int, float])
        self.assertEqual(result, ['My_work', 20, 100.5])
        self.assertTrue(isinstance(result, list))
        self.assertFalse(isinstance(result, int))

    def test_delimiter(self):
        result = split('My_work/20/100.500', [str, int, float], '/')
        self.assertEqual(result, ['My_work', 20, 100.5])



if __name__ == '__main__':
    unittest.main()