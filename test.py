import unittest
from assignment import calculate_mean, calculate_median, calculate_mode

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 2, 3, 4, 5, 5, 5, 6]

    def test_mean(self):
        self.assertAlmostEqual(calculate_mean(self.data), 3.6666666666666665)

    def test_median(self):
        self.assertEqual(calculate_median(self.data), 4)

    def test_mode(self):
        self.assertEqual(sorted(calculate_mode(self.data)), [5])

if __name__ == '__main__':
    unittest.main()
