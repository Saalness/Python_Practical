import unittest

from FloydWarshallRecursive import function_j
from FloydWarshallRecursive import check_increments

class Testing(unittest.TestCase):

    def test_output_matrix(self):
       self.assertEqual(function_j(dist), output, "the two lists should match")

    def test_increments(self):
        self.assertEqual(check_increments(), 4, "k should loop 4 times")

graph = [[0, 5, 999, 10],
         [999, 0, 3, 999],
         [999, 999, 0,   1],
         [999, 999, 999, 0]
         ]
dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
output =[[0, 5, 8, 9],
         [999, 0, 3, 4],
         [999, 999, 0, 1],
         [999, 999, 999, 0]]