import unittest
from Pencil import Pencil

class TestPencil(unittest.TestCase):
    def setUp(self):
        self.pencil = Pencil(100,5,99)
        self.pencil2 = Pencil(50, 10, 110)


class TestInit(TestPencil):
    def test_initial_point_durability(self):
        self.assertEqual(self.pencil.initial_point_durability, 100)
        self.assertEqual(self.pencil2.initial_point_durability, 50)

    def test_current_point_durability_before_writing(self):
        self.assertEqual(self.pencil.current_point_durability, 100)
        self.assertEqual(self.pencil2.current_point_durability, 50)

    def test_initial_eraser_durability(self):
        self.assertEqual(self.pencil.eraser_durability, 99)
        self.assertEqual(self.pencil2.eraser_durability, 110)

    def test_initial_pencil_length(self):
        self.assertEqual(self.pencil.pencil_length, 5)
        self.assertEqual(self.pencil2.pencil_length, 10)


class TestWrite(TestPencil):
    def test_write_to_empty(self):
        self.assertEqual(self.pencil.write("", "the lazy dog"), "the lazy dog")

    def test_write_to_non_empty(self):
        self.assertEqual(self.pencil.write("the lazy dog ", "jumped over the fox"), "the lazy dog jumped over the fox")

    def test_write_while_point_at_0(self):
        self.pencil.current_point_durability = 0
        self.assertEqual("Hello, Wor  ", self.pencil.write("Hello, Wor", "ld"))

    def test_write_to_point_degradation(self):
        self.pencil.current_point_durability = 6
        self.assertEqual("Hello     ", self.pencil.write("", "HelloWorld"))

    def test_write_to_point_degradation_with_spaces(self):
        self.pencil.current_point_durability = 6
        self.assertEqual("Hello       ", self.pencil.write("", "Hello, World"))

class TestPointDegradation(TestPencil):
    def test_point_degradation_capital(self):
        self.pencil.write("","A")
        self.assertEqual(self.pencil.current_point_durability, self.pencil.initial_point_durability-2)

    def test_point_degradation_lowercase(self):
        self.pencil.write("","a")
        self.assertEqual(self.pencil.current_point_durability, self.pencil.initial_point_durability-1)

    def test_point_degradation_number(self):
        self.pencil.write("","1")
        self.assertEqual(self.pencil.current_point_durability, self.pencil.initial_point_durability-1)

    def test_point_degradation_symbol(self):
        self.pencil.write("","$")
        self.assertEqual(self.pencil.current_point_durability, self.pencil.initial_point_durability-1)

    def test_point_degradation_space(self):
        self.pencil.write("", " ")
        self.assertEqual(self.pencil.current_point_durability, self.pencil.initial_point_durability)

    def test_point_degradation_space(self):
        self.pencil.write("", "\n")
        self.assertEqual(self.pencil.current_point_durability, self.pencil.initial_point_durability)

    def test_point_degradation_string(self):
        self.pencil.write("","The Lazy Dog") #3 capitals = 6, 7 lowercase = 7
        self.assertEqual(self.pencil.current_point_durability, self.pencil.initial_point_durability - 13)

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

class TestErase(TestPencil):
    def test_erase_text_on_page(self):
        pass

    def test_erase_text_not_on_page(self):
        pass

    def test_eraser_degradation_without_white_space(self):
        pass

    def test_eraser_degradation_with_white_space(self):
        pass

    def test_erase_text_while_degraded_eraser(self):
        pass

    def test_erase_text_to_degraded_eraser(self):
        # test the case where the eraser becomes degraded while erasing
        pass

if __name__ == '__main__':
	unittest.main()
