class Pencil:

    def __init__(self, point_durability, pencil_length, eraser_durability):
        self.initial_point_durability = point_durability
        self.current_point_durability = point_durability
        self.pencil_length = pencil_length
        self.eraser_durability = eraser_durability

    # User Callable Method -- All of the Logic is in the WriteHelper and WriteCharacters Private Methods
    def write(self, text_on_page, text_to_be_written):
        return self._write_helper(text_on_page, text_to_be_written, len(text_on_page))

    # A Helper Method To Allow Both the Write and Edit Functions To Use
    def _write_helper(self, text_on_page, text_to_be_written, start_index):
        written_text = ""
        current_index = start_index
        for char_to_write in text_to_be_written:
            if current_index < len(text_on_page):  # if an edit in between a string
                current_character = text_on_page[current_index]
                written_text += self._write_characters_edit(current_character, char_to_write)
                current_index += 1
            else:  # if appending to the page, just write the characters
                written_text += self._write_characters(char_to_write)

        return text_on_page[0: start_index] + written_text

    def _write_characters_edit(self, current_character, char_to_write):
        if current_character != '\n' and current_character != ' ':  # collision
            if self.current_point_durability > 0:  # if the pencil has a point
                self.current_point_durability -= 1
                return '@'
            else:  # no point, we can't write anything so the page stays as is
                return current_character
        else:  # if no collision, write the character in the space and degrade the point
            return self._write_characters(char_to_write)

    # A Helper Method To Determine What Kind Of Character/Response is Required When Writing
    def _write_characters(self, char_to_write):
        if self.current_point_durability <= 0:
            return " "
        elif char_to_write.isupper():
            if self.current_point_durability > 1:  # if durability was at 1, we can't write an uppercase
                self.current_point_durability -= 2
                return char_to_write
            else:
                return " "
        elif char_to_write == ' ' or char_to_write == '\n':
            return char_to_write
        else:
            self.current_point_durability -= 1
            return char_to_write

    # User Callable Method to Erase -- All of the Logic is in the EraseHelper Method
    def erase(self, text_on_page, text_to_erase):
        word_erased_index, new_text = self._erase_helper(text_on_page, text_to_erase)
        if word_erased_index == -1:
            return text_on_page
        else:
            return new_text.rstrip()

    # A Helper Method To Allow Both the Erase and Edit Functions to Use It
    def _erase_helper(self, text_on_page, text_to_erase):
        text_to_erase.strip(" ")
        text_to_erase.strip("\n")
        word_to_erase_index = text_on_page.lower().rfind(text_to_erase.lower())  # index where the word was found.
        if word_to_erase_index == -1 or len(text_to_erase) < 1:  # if the word wasn't found, we do nothing
            return -1, ""
        erased_space = self._erase_characters(word_to_erase_index, text_on_page, text_to_erase)
        text_before_erase = text_on_page[0: word_to_erase_index + len(text_to_erase) - len(erased_space)]
        text_after_erase = text_on_page[word_to_erase_index + len(text_to_erase):]
        return word_to_erase_index, text_before_erase + erased_space + text_after_erase

    # A Helper Method to Calculate the Number of Erased Spaces
    def _erase_characters(self, word_to_erase_index, text_on_page, text_to_erase):
        erased_space = ""
        erase_start_index = word_to_erase_index + len(text_to_erase) - 1
        for i in range(erase_start_index, word_to_erase_index - 1, -1):
            if text_on_page[i] == ' ' or text_on_page[i] == '\n':
                erased_space += text_on_page[i]
                continue
            if self.eraser_durability > 0:
                erased_space += " "
                self.eraser_durability -= 1
            else:  # we erase until the eraser breaks
                break
        return erased_space

    # User Callable Method to sharpen the pencil
    def sharpen(self):
        if self.pencil_length >= 1 and self.current_point_durability != self.initial_point_durability:
            self.current_point_durability = self.initial_point_durability
            self.pencil_length -= 1
        else:
            print("Can't sharpen this pencil!")

    # User Callable Method to edit code -- Logic is based on both _write_helper and _erase_helper
    def edit(self, text_on_page, text_to_edit, text_to_replace_with):
        index, after_erase_text = self._erase_helper(text_on_page, text_to_edit)
        if index == -1:
            return text_on_page
        edited_text = self._write_helper(after_erase_text, text_to_replace_with, index)
        return edited_text + after_erase_text[index + len(text_to_replace_with):].rstrip()
