class Pencil:

    def __init__(self, point_durability, pencil_length, eraser_durability):
        self.initial_point_durability = point_durability
        self.current_point_durability = point_durability
        self.pencil_length = pencil_length
        self.eraser_durability = eraser_durability

    def write(self, text_on_page, text_to_be_written):
        new_text = ""
        for char in text_to_be_written:
            if self.current_point_durability == 0:
                new_text += " "
            elif (char.isupper()):
                self.current_point_durability -= 2 #revisit what we do if durability is at 1
                new_text += char
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
