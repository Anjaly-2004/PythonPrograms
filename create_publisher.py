class Publisher:
    def __init__(self, publisher):
        self.publisher = publisher


class Book(Publisher):
    def __init__(self, publisher, title, author):
        super().__init__(publisher)
        self.title = title
        self.author = author

    def display(self):
        print("Publisher:", self.publisher)
        print("Book Title:", self.title)
        print("Author:", self.author)


class Python(Book):
    def __init__(self, publisher, title, author, price):
        super().__init__(publisher, title, author)
        self.price = price

    # Method overriding
    def display(self):
        super().display()
        print("Price:", self.price)


# Creating Python book object
p = Python("ABC Publications", "Python Programming",
           "John Smith", 450)

# Display book information
p.display()
