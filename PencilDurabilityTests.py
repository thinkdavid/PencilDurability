import unittest

from Pencil import Pencil


class TestPencil(unittest.TestCase):
    def setUp(self):
        self.pencil = Pencil(100, 5, 99)
        self.pencil_2 = Pencil(20, 3, 30)


class TestInit(TestPencil):
    def test_initial_point_durability(self):
        self.assertEqual(self.pencil.initial_point_durability, 100)
        self.assertEqual(self.pencil_2.initial_point_durability, 20)

    def test_current_point_durability_before_writing(self):
        self.assertEqual(self.pencil.current_point_durability, 100)
        self.assertEqual(self.pencil_2.current_point_durability, 20)

    def test_initial_eraser_durability(self):
        self.assertEqual(self.pencil.eraser_durability, 99)
        self.assertEqual(self.pencil_2.eraser_durability, 30)

    def test_initial_pencil_length(self):
        self.assertEqual(self.pencil.pencil_length, 5)
        self.assertEqual(self.pencil_2.pencil_length, 3)


class TestWrite(TestPencil):
    def test_write_to_empty(self):
        self.assertEqual(self.pencil.write("", "the lazy dog"), "the lazy dog")

    def test_write_to_non_empty(self):
        self.assertEqual(self.pencil.write("the lazy dog ", "jumped over the fox"), "the lazy dog jumped over the fox")

    def test_write_white_spaces(self):
        self.assertEqual(self.pencil.write("", "    the lazy dog  "), "    the lazy dog  ")

    def test_write_while_point_at_0(self):
        self.pencil.current_point_durability = 0
        self.assertEqual("Hello, Wor  ", self.pencil.write("Hello, Wor", "ld"))

    def test_write_capital_while_point_at_1(self):
        self.pencil.current_point_durability = 1
        self.assertEqual("Hello,  ", self.pencil.write("Hello,", " W"))

    def test_write_capital_while_point_at_1_with_lowerCase_after(self):
        self.pencil.current_point_durability = 1
        self.assertEqual(" e   ", self.pencil.write("", "Hello"))
        self.pencil.current_point_durability = 1
        self.assertEqual("  e   ", self.pencil.write("", "H ello"))

    def test_write_to_point_degradation(self):
        self.pencil.current_point_durability = 6
        self.assertEqual("Hello     ", self.pencil.write("", "HelloWorld"))

    def test_write_to_point_degradation_with_spaces(self):
        self.pencil.current_point_durability = 6
        self.assertEqual("Hello       ", self.pencil.write("", "Hello, World"))


class TestPointDegradation(TestPencil):
    def test_point_degradation_capital(self):
        self.pencil.write("", "A")
        self.assertEqual(self.pencil.current_point_durability, self.pencil.initial_point_durability - 2)

    def test_point_degradation_lowercase(self):
        self.pencil.write("", "a")
        self.assertEqual(self.pencil.current_point_durability, self.pencil.initial_point_durability - 1)

    def test_point_degradation_number(self):
        self.pencil.write("", "1")
        self.assertEqual(self.pencil.current_point_durability, self.pencil.initial_point_durability - 1)

    def test_point_degradation_symbol(self):
        self.pencil.write("", "$")
        self.assertEqual(self.pencil.current_point_durability, self.pencil.initial_point_durability - 1)

    def test_point_degradation_space(self):
        self.pencil.write("", " ")
        self.assertEqual(self.pencil.current_point_durability, self.pencil.initial_point_durability)

    def test_point_degradation_space(self):
        self.pencil.write("", "\n")
        self.assertEqual(self.pencil.current_point_durability, self.pencil.initial_point_durability)

    def test_point_degradation_string(self):
        self.pencil.write("", "The Lazy Dog")  # 3 capitals = 6, 7 lowercase = 7
        self.assertEqual(self.pencil.current_point_durability, self.pencil.initial_point_durability - 13)


class TestSharpen(TestPencil):
    def test_sharpen_durability(self):
        self.pencil.current_point_durability -= 4
        self.pencil.sharpen()
        self.assertEqual(self.pencil.current_point_durability, self.pencil.initial_point_durability)

    def test_sharpen_if_pencil_at_full_durability(self):
        old_length = self.pencil.pencil_length
        self.pencil.sharpen()
        self.assertEqual(old_length, self.pencil.pencil_length)

    def test_sharpen_length(self):
        old_length = self.pencil.pencil_length
        self.pencil.current_point_durability -= 4
        self.pencil.sharpen()
        self.assertEqual(old_length - 1, self.pencil.pencil_length)

    def test_sharpen_pencil_with_length_0(self):
        self.pencil.pencil_length = 0
        self.pencil.current_point_durability -= 4
        old_durability = self.pencil.current_point_durability
        self.pencil.sharpen()
        self.assertEqual(self.pencil.current_point_durability, old_durability)

    def test_decrement_of_pencil_length_to_0(self):
        self.pencil.pencil_length = 1
        self.pencil.current_point_durability -= 4
        self.pencil.sharpen()
        self.pencil.current_point_durability -= 4
        self.pencil.sharpen()
        self.assertEqual(self.pencil.initial_point_durability - 4, self.pencil.current_point_durability)


class TestErase(TestPencil):
    def test_erase_text_on_page(self):
        self.assertEqual(self.pencil.erase("The Lazy Dog Jumped Over The Fence", "Fence"),
                         "The Lazy Dog Jumped Over The")
        self.assertEqual(self.pencil.erase("The Lazy Dog Jumped Over The Fence", "og"),
                         "The Lazy D   Jumped Over The Fence")
        self.assertEqual(self.pencil.erase("The Lazy Dog Jumped Over The Fence", "he"),
                         "The Lazy Dog Jumped Over T   Fence")
        self.assertEqual(self.pencil.erase("The Lazy Dog Jumped Over A Fence", "The"),
                         "    Lazy Dog Jumped Over A Fence")
        self.assertEqual(
            self.pencil.erase("How much wood would a woodchuck chuck if a woodchuck could       wood", "chuck"),
            "How much wood would a woodchuck chuck if a wood      could       wood")

    def test_erase_text_not_on_page(self):
        self.assertEqual(self.pencil.erase("The Lazy Dog Jumped Over The Fence", "Animals"),
                         "The Lazy Dog Jumped Over The Fence")
        self.assertEqual(self.pencil.erase("The Lazy Dog Jumped Over The Fence", "abc"),
                         "The Lazy Dog Jumped Over The Fence")

    def test_erase_wrong_case(self):
        self.assertEqual(self.pencil.erase("Hello, world!", "hello"), "     , world!")
        self.assertEqual(self.pencil.erase("Hello, world!", "HELLO"), "     , world!")
        self.assertEqual(self.pencil.erase("Hello, world!", "HeLlO"), "     , world!")

    def test_eraser_erase_str_with_white_space(self):
        self.assertEqual(self.pencil.erase("The Lazy Dog Jumped Over The Fence", "e Fence"),
                         "The Lazy Dog Jumped Over Th")

    def test_eraser_erase_white_space(self):
        self.assertEqual(self.pencil.erase("The Lazy Dog Jumped Over The Fence", " "),
                         "The Lazy Dog Jumped Over The Fence")
        self.assertEqual(self.pencil.erase("The Lazy Dog Jumped Over The Fence", "  "),
                         "The Lazy Dog Jumped Over The Fence")
        self.assertEqual(self.pencil.erase("The Lazy Dog \n Jumped Over The Fence", "\n"),
                         "The Lazy Dog \n Jumped Over The Fence")
        self.assertEqual(self.pencil.erase("The Lazy Dog \n Jumped Over The Fence", "\n\n"),
                         "The Lazy Dog \n Jumped Over The Fence")

    def test_eraser_passed_empty_string_to_erase(self):
        self.assertEqual(self.pencil.erase("The Lazy Dog Jumped Over The Fence", ""),
                         "The Lazy Dog Jumped Over The Fence")

    def test_eraser_passed_empty_string_on_paper(self):
        self.assertEqual(self.pencil.erase("", "Hello"),
                         "")

    def test_eraser_degradation_without_white_space(self):
        before_eraser = self.pencil.eraser_durability
        self.pencil.erase("The Lazy Dog Jumped Over The Fence", "Fence")
        self.assertEqual(before_eraser - 5, self.pencil.eraser_durability)

    def test_eraser_degradation_with_white_space(self):
        before_eraser = self.pencil.eraser_durability
        self.pencil.erase("The Lazy Dog Jumped Over The Fence", "e Fence")
        self.assertEqual(before_eraser - 6, self.pencil.eraser_durability)

    def test_erase_text_while_degraded_eraser(self):
        self.pencil.eraser_durability = 0
        self.assertEqual(self.pencil.erase("The Lazy Dog Jumped Over The Fence", "The"),
                         "The Lazy Dog Jumped Over The Fence")

    def test_erase_text_to_degraded_eraser(self):
        # test the case where the eraser becomes degraded while erasing
        self.pencil.eraser_durability = 2
        self.assertEqual(self.pencil.erase("The Lazy Dog Jumped Over The Fence", "The"),
                         "The Lazy Dog Jumped Over T   Fence")


class TestEdit(TestPencil):
    def test_edit_by_replacing_word(self):
        edited_string = self.pencil.edit("Hello, World", "World", "Accenture")
        self.assertEqual(edited_string, "Hello, Accenture")
        edited_string = self.pencil.edit("Hello, World", "ello", "i")
        self.assertEqual(edited_string, "Hi   , World")

    def test_edit_by_replacing_with_longer_string(self):
        edited_string = self.pencil.edit("Hello, World", "ello, World", "i, Y'all")
        self.assertEqual(edited_string, "Hi, Y'all")
        edited_string = self.pencil.edit("New City Road", "New City", "Old Town")
        self.assertEqual(edited_string, "Old Town Road")

    def test_edit_with_collisions(self):
        edited_string = self.pencil.edit("Hi World", "Hi", "Hello,")
        self.assertEqual(edited_string, "Hel@@@ld")
        edited_string = self.pencil.edit("An apple a day keeps the doctor away", "apple", "artichoke")
        self.assertEqual(edited_string, "An artich@k@ay keeps the doctor away")

    def test_edit_with_degraded_point(self):
        self.pencil.current_point_durability = 0
        edited_string = self.pencil.edit("Hi World", "orl", "izar")
        self.assertEqual(edited_string, "Hi W   d")  # no point so no collision

    def test_edit_with_degraded_eraser(self):
        self.pencil.eraser_durability = 0
        edited_string = self.pencil.edit("Hi World", "orl", "izar")
        self.assertEqual(edited_string, "Hi W@@@@")

    def test_edit_with_point_becoming_degraded(self):
        self.pencil.current_point_durability = 2
        edited_string = self.pencil.edit("Hi World", "orl", "izar")
        self.assertEqual(edited_string, "Hi Wiz d")  # no point so no collision

    def test_edit_with_eraser_becoming_degraded(self):
        self.pencil.eraser_durability = 2
        edited_string = self.pencil.edit("Hi World", "orl", "izar")
        self.assertEqual(edited_string, "Hi W@za@")  # no point so no collision

    def test_edit_with_both_becoming_degraded(self):
        self.pencil.current_point_durability = 2
        self.pencil.eraser_durability = 2
        edited_string = self.pencil.edit("Hi World", "orl", "izar")
        self.assertEqual(edited_string, "Hi W@z d")  # no point so no collision

    def test_edit_with_word_not_found(self):
        edited_string = self.pencil.edit("I Love Pancakes", "abc", "Sunshine")
        self.assertEqual(edited_string, "I Love Pancakes")

    def test_edit_with_start_in_page_continue_to_new(self):
        # basically test when we start the edit inside the text on the page, then go into new
        edited_string = self.pencil.edit("I Love Pancakes", "Pancakes",
                                         "Waffles, mostly, but Pancakes are a solid choice")
        self.assertEqual(edited_string, "I Love Waffles, mostly, but Pancakes are a solid choice")


if __name__ == '__main__':
    unittest.main()
