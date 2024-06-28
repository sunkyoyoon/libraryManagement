# models.py

class Book:
    def __init__(self, title, author, isbn, id=None):
        self.id = id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

class Library:
    def __init__(self, database):
        self.database = database

    def add_book(self, book):
        return self.database.add_book(book)

    def remove_book(self, book_id):
        return self.database.remove_book(book_id)

    def get_book(self, book_id):
        return self.database.get_book(book_id)

    def list_books(self):
        return self.database.list_books()

    def search_books(self, keyword):
        return self.database.search_books(keyword)

    def borrow_book(self, book_id):
        book = self.get_book(book_id)
        if book and not book.is_borrowed:
            book.is_borrowed = True
            return self.database.update_book(book)
        return False

    def return_book(self, book_id):
        book = self.get_book(book_id)
        if book and book.is_borrowed:
            book.is_borrowed = False
            return self.database.update_book(book)
        return False