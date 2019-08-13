class Pencil:

    def __init__(self, point_durability, pencil_length, eraser_durability):
        self.initial_point_durability = point_durability
        self.current_point_durability = point_durability
        self.pencil_length = pencil_length
        self.eraser_durability = eraser_durability

    def write(self, text_on_page, text_to_be_written):
        new_text = ""
        for char in text_to_be_written:
            if self.current_point_durability <= 0:
                new_text += " "
            elif (char.isupper()):
                if self.current_point_durability > 1: #if durability was at 1, we can't write an uppercase
                    self.current_point_durability -= 2
                    new_text += char
                else:
                    new_text += " "
            elif(char == ' ' or char == '\n'):
                self.current_point_durability -= 0
                new_text += char
            else:
                self.current_point_durability -= 1
                new_text += char

        return text_on_page + new_text

    def sharpen(self):
        if self.pencil_length > 1:
            self.current_point_durability = self.initial_point_durability
            self.pencil_length -= 1
        else:
            print("The pencil is too short to sharpen!")

    def erase(self, text_on_page, text_to_erase):
        index, new_text = self.eraseHelper(text_on_page, text_to_erase)
        if index == -1:
            return text_on_page
        else:
            return text_on_page[0: index + len(text_to_erase) - len(new_text)] \
               + new_text \
               + text_on_page[index+len(text_to_erase):]

    def eraseHelper(self, text_on_page, text_to_erase):
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

        return ((index, new_text))


    def edit(self, text_on_page, text_to_edit, text_to_replace):

        after_erase = self.erase(text_on_page, text_to_edit)

