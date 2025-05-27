class Book:
    def __init__(self, title, author, pages=1):
        self.title = title
        self.author = author
        self.pages = pages  # uses setter

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
            return
        if value <= 0:
            print("page_count must be positive")
            return
        self._pages = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"
