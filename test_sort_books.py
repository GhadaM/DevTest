from unittest import TestCase
from books import sort_books


class TestSortBooks(TestCase):
    def test_sort_books(self):
        self.assertEqual(sort_books([3, 1, 5, 4, 2]), 3)
        self.assertEqual(sort_books([7, 6, 5, 4, 3, 2, 1]), 3)
