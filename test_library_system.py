# test_library_system.py

import unittest
from models import Book, Library
from database import Database

class TestLibrarySystem(unittest.TestCase):
    def setUp(self):
        self.database = Database(':memory:')
        self.library = Library(self.database)
        self.book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
        self.book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780446310789")

    def test_add_book(self):
        self.assertTrue(self.library.add_book(self.book1))
        self.assertEqual(len(self.library.list_books()), 1)

    def test_remove_book(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        book_id = self.library.list_books()[0].id
        self.assertTrue(self.library.remove_book(book_id))
        self.assertEqual(len(self.library.list_books()), 1)

    def test_borrow_book(self):
        self.library.add_book(self.book1)
        book_id = self.library.list_books()[0].id
        self.assertTrue(self.library.borrow_book(book_id))
        self.assertFalse(self.library.borrow_book(book_id))

    def test_return_book(self):
        self.library.add_book(self.book1)
        book_id = self.library.list_books()[0].id
        self.library.borrow_book(book_id)
        self.assertTrue(self.library.return_book(book_id))
        self.assertFalse(self.library.return_book(book_id))

    def test_list_books(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.assertEqual(len(self.library.list_books()), 2)

    def test_search_books(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.assertEqual(len(self.library.search_books("Gatsby")), 1)
        self.assertEqual(len(self.library.search_books("Harper")), 1)

if __name__ == '__main__':
    unittest.main()