import unittest
import quick_sort
from sort_utility import is_list_sorted


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.vectors = [range(10, 0, -1),
                        [1, 3, 5, 2, 4, 6],
                        ["abc", "aab", "caa", "-**"],
                        [True, False, True],
                        [],
                        ["a", "a", "c", "a"],
                        [1],
                        [2, 1],
                        [3, 2, 1]]

    def test_vector(self):
        for test_vector in self.vectors:
            quick_sort.quick_sort(test_vector)
            self.assertTrue(is_list_sorted(test_vector))


if __name__ == '__main__':
    unittest.main()
