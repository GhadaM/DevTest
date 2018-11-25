from unittest import TestCase

from searching import searching_element


class TestSearchingElement(TestCase):
    def test_searching_element(self):
        self.assertEqual(searching_element([7, 8, 9, 1, 4, 6], 3), False)
        self.assertEqual(searching_element([1, 2, 3, 4, 5, 6, 0], 5), True)