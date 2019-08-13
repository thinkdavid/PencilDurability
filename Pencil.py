class Pencil:

    def __init__(self, point_durability, pencil_length, eraser_durability):
        self.initial_point_durability = point_durability
        self.current_point_durability = point_durability
        self.pencil_length = pencil_length
        self.eraser_durability = eraser_durability

    # A Helper Method To Allow Both the Write and Edit Functions To Use
    def _write_helper(self, text_on_page, text_to_be_written, start_index):
        new_text = ""
        page_index = start_index
        for char in text_to_be_written:
            if page_index < len(text_on_page):
                if text_on_page[page_index] != '\n' and text_on_page[page_index] != ' ':
                    if self.current_point_durability > 0:
                        new_text += '@'
                        self.current_point_durability -= 1
                    else:
                        new_text += text_on_page[page_index]
                else:
                    new_text = self._write_characters(new_text, char)
                page_index += 1
            else:
                new_text = self._write_characters(new_text, char)

        return text_on_page[0: start_index] + new_text

    # A Helper Method To Determine What Kind Of Character/Response is Required When Writing
    def _write_characters(self, new_text, char):
        if self.current_point_durability <= 0:
            new_text += " "
        elif (char.isupper()):
            if self.current_point_durability > 1:  # if durability was at 1, we can't write an uppercase
                self.current_point_durability -= 2
                new_text += char
            else:
                new_text += " "
        elif (char == ' ' or char == '\n'):
            self.current_point_durability -= 0
            new_text += char
        else:
            self.current_point_durability -= 1
            new_text += char
        return new_text

    # User Callable Method -- All of the Logic is in the WriteHelper and WriteCharacters Private Methods
    def write(self, text_on_page, text_to_be_written):
        return self._write_helper(text_on_page, text_to_be_written, len(text_on_page))

    # User Callable Method to sharpen the pencil
    def sharpen(self):
        if self.pencil_length > 1:
            self.current_point_durability = self.initial_point_durability
            self.pencil_length -= 1
        else:
            print("The pencil is too short to sharpen!")

    # A Helper Method To Allow Both the Erase and Edit Functions to Use It
    def _erase_helper(self, text_on_page, text_to_erase):
        text_to_erase.strip(" ")
        text_to_erase.strip("\n")
        index = text_on_page.rfind(text_to_erase)  # index where the word was found.
        if index == -1 or len(text_to_erase) < 1:
            return ((-1, ""))
        new_text = ""  # the number of erased characters
        for i in range(index + len(text_to_erase) - 1, index - 1, -1):  # the string length is the max amount of erasure
            if text_on_page[i] == ' ' or text_on_page[i] == '\n':
                new_text += text_on_page[i]
                continue
            if self.eraser_durability > 0:
                new_text += " "
                self.eraser_durability -= 1
            else:
                break

        return ((index, text_on_page[0: index + len(text_to_erase) - len(new_text)] \
                   + new_text \
                   + text_on_page[index + len(text_to_erase):]))

    # User Callable Method to Erase -- All of the Logic is in the EraseHelper Method
    def erase(self, text_on_page, text_to_erase):
        index, new_text = self._erase_helper(text_on_page, text_to_erase)
        if index == -1:
            return text_on_page
        else:
            return new_text.rstrip()

    #User Callable Method to edit code -- Logic is based on both _write_helper and _erase_helper
    def edit(self, text_on_page, text_to_edit, text_to_replace_with):
        index, after_erase_text = self._erase_helper(text_on_page, text_to_edit)
        if index == -1:
            return text_on_page
        edited_text = self._write_helper(after_erase_text, text_to_replace_with, index)
        return edited_text + after_erase_text[index + len(text_to_replace_with):].rstrip()
