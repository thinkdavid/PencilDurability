class Pencil:

    def __init__(self, point_durability, pencil_length, eraser_durability):
        self.initial_point_durability = point_durability
        self.current_point_durability = point_durability
        self.pencil_length = pencil_length
        self.eraser_durability = eraser_durability

    def write(self, text_on_page, text_to_be_written):
        for char in text_to_be_written:
            if (char.isupper()):
                self.current_point_durability -= 2
            elif(char == ' ' or char == '\n'):
                self.current_point_durability -= 0
            else:
                self.current_point_durability -= 1

        return text_on_page + text_to_be_written

    def sharpen(self):
        if self.pencil_length > 1:
            self.current_point_durability = self.initial_point_durability
            self.pencil_length -= 1
        else:
            print("The pencil is too short to sharpen!")
