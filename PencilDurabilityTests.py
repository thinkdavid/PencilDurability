import unittest
from Pencil import Pencil

class TestPencil(unittest.TestCase):
      def setUp(self):
          self.pencil = Pencil(10,5,9)


class TestInit(TestPencil):
      def test_initial_point_durability(self):
          self.assertEqual(self.pencil.point_durability, 10)

      def test_initial_eraser_durability(self):
          self.assertEqual(self.pencil.eraser_durability, 9)

      def test_initial_pencil_length(self):
          self.assertEqual(self.pencil.pencil_length, 5)


class TestWrite(TestPencil):
      def test_write_to_empty(self):
          self.assertEqual(self.pencil.write("", "the lazy dog"), "the lazy dog")

      def test_write_to_non_empty(self):
          self.assertEqual(self.pencil.write("the lazy dog ", "jumped over the fox"), "the lazy dog jumped over the fox")


if __name__ == '__main__':
    unittest.main()
