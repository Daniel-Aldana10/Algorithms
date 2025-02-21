import unittest
from sorting_algorithms import bubblesort
from sorting_algorithms import mergesort
from sorting_algorithms import shellsort

arrays = [
    [1, 9, 8, 2, 3, 4, 5, 7, 6],
    [1],
    [2],
    [2, 1],
    [1, 2],
    [4, 6, 2],
    [1, 3, 9],
    [10, 8],
    [11, 31],
    [],
    [-1, 5, -512, 1],
    [100, 50, 25, 75, 10],
    [0, 0, 0, 0],
    [99, -99, 0],
    [5, 3, 1, 9, 7, 2, 8, 6, 4],
    [-5, -10, -3, -7, -1, -9, -2, -8, -4, -6],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [3, 5, 7, 1, 2, 4]
]
expected = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1],
    [2],
    [1, 2],
    [1, 2],
    [2, 4, 6],
    [1, 3, 9],
    [8, 10],
    [11, 31],
    [],
    [-512, -1, 1, 5],
    [10, 25, 50, 75, 100],
    [0, 0, 0, 0],
    [-99, 0, 99],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 7]
]
class AlgorithmsTests(unittest.TestCase):
    def test_split_and_sorted_approach(self):
        for i in range(len(arrays)):
            array = arrays[i]
            result = bubblesort.bubblesort(array)
            self.assertEqual(result, expected[i])

    def test_no_split_and_sorted_approach(self):
        for i in range(len(arrays)):
            array = arrays[i]
            result = mergesort.mergesort(array)
            self.assertEqual(result, expected[i])

    def test_full_sort_and_iterate_approach(self):
        for i in range(len(arrays)):
            array = arrays[i]
            result = shellsort.shellsort(array)
            self.assertEqual(result, expected[i])


if __name__ == "__main__":
    unittest.main()
