class Shoe:
    def __init__(self, brand, size, color=None):
        self.brand = brand
        self.color = color
        self.condition = "Used"
        self.size = size  # use setter

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
            return
        if value <= 0:
            print("size must be a positive number")
            return
        self._size = value

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

    def __str__(self):
        color_str = self.color if self.color else "Unknown color"
        return f"{color_str} {self.brand} shoe, size {self.size}"
