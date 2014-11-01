import unittest
import order_statistics


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.vectors = [(range(1000), 499, 499),
                        (range(10, 0, -1), 4, 5),
                        ([1, 3, 5, 2, 4, 6], 3, 4),
                        (["abc", "aab", "caa", "-**"], 1, "aab"),
                        ([True, False, True], 0, False),
                        ([], 0, None)]

    def test_vector(self):
        for test_vector in self.vectors:
            order_stat = order_statistics.order_statistics(test_vector[0],
                                                           test_vector[1])
            self.assertEqual(order_stat, test_vector[2])


if __name__ == '__main__':
    unittest.main()
