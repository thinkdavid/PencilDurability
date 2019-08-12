class Pencil:

    def __init__(self, point_durability, pencil_length, eraser_durability):
        self.point_durability = point_durability
        self.pencil_length = pencil_length
        self.eraser_durability = eraser_durability

    def write(self, text_on_page, text_to_be_written):
        return text_on_page + text_to_be_written
