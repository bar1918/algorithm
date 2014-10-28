import unittest
import count_inversions


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.vectors = [(range(1000), 0),
                        (range(10, 0, -1), 45),
                        ([1, 3, 5, 2, 4, 6], 3),
                        (["abc", "aab", "caa", "-**"], 4),
                        ([True, False, True], 1),
                        ([], 0)]

    def test_vector(self):
        for test_vector in self.vectors:
            inv, list = count_inversions.count_inversions(test_vector[0])
            self.assertEqual(inv, test_vector[1])


if __name__ == '__main__':
    unittest.main()
