import unittest
from Pencil import Pencil

class TestPencil(unittest.TestCase):
    def setUp(self):
        self.pencil = Pencil(10,5,9)


class TestInit(TestPencil):
    def test_initial_point_durability(self):
        self.assertEqual(self.pencil.initial_point_durability, 10)

    def test_initial_point_durability(self):
        self.assertEqual(self.pencil.current_point_durability, 10)

    def test_initial_eraser_durability(self):
        self.assertEqual(self.pencil.eraser_durability, 9)

    def test_initial_pencil_length(self):
        self.assertEqual(self.pencil.pencil_length, 5)


class TestWrite(TestPencil):
    def test_write_to_empty(self):
        self.assertEqual(self.pencil.write("", "the lazy dog"), "the lazy dog")

    def test_write_to_non_empty(self):
        self.assertEqual(self.pencil.write("the lazy dog ", "jumped over the fox"), "the lazy dog jumped over the fox")

class TestSharpen(TestPencil):
    def test_sharpen_durability(self):
        self.pencil.current_point_durability -= 4
        self.pencil.sharpen()
        self.assertEqual(self.pencil.current_point_durability, self.pencil.initial_point_durability)

    def test_sharpen_length(self):
        old_length = self.pencil.pencil_length
        self.pencil.sharpen()
        self.assertEqual(old_length-1, self.pencil.pencil_length)

    def test_sharpen_pencil_with_length_0(self):
        self.pencil.pencil_length = 0
        self.pencil.current_point_durability -= 4
        old_durability = self.pencil.current_point_durability
        self.pencil.sharpen()
        self.assertEqual(self.pencil.current_point_durability, old_durability)


if __name__ == '__main__':
	unittest.main()
