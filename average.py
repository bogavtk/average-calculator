import unittest

def average(numberArray):
    return sum(numberArray) / len(numberArray)

class TestAverage(unittest.TestCase):

    def test_average_with_positive_numbers(self):
        numbers = [1, 2, 3, 4, 5]
        expected_result = 3.0
        self.assertEqual(average(numbers), expected_result)

    def test_average_with_negative_numbers(self):
        numbers = [-1, -2, -3, -4, -5]
        expected_result = -3.0
        self.assertEqual(average(numbers), expected_result)

    def test_average_with_mixed_positive_and_negative_numbers(self):
        numbers = [1, -2, 3, -4, 5]
        expected_result = 0.6
        self.assertAlmostEqual(average(numbers), expected_result, places=1)

    def test_average_with_empty_list(self):
        numbers = []
        # You can define the expected behavior for an empty list,
        # in this case, let's assume it returns None.
        expected_result = None
        self.assertIsNone(average(numbers))

    def test_average_with_single_number(self):
        numbers = [10]
        expected_result = 10.0
        self.assertEqual(average(numbers), expected_result)

if __name__ == '__main__':
    unittest.main()