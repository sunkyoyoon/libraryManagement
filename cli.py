# cli.py

from models import Book, Library
from database import Database

class CLI:
    def __init__(self):
        self.database = Database()
        self.library = Library(self.database)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            self.handle_choice(choice)

    def display_menu(self):
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. List all books")
        print("4. Search for a book")
        print("5. Borrow a book")
        print("6. Return a book")
        print("7. Exit")

    def handle_choice(self, choice):
        if choice == '1':
            self.add_book()
        elif choice == '2':
            self.remove_book()
        elif choice == '3':
            self.list_books()
        elif choice == '4':
            self.search_books()
        elif choice == '5':
            self.borrow_book()
        elif choice == '6':
            self.return_book()
        elif choice == '7':
            print("Thank you for using the Library Management System.")
            exit()
        else:
            print("Invalid choice. Please try again.")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        isbn = input("Enter book ISBN: ")
        book = Book(title, author, isbn)
        if self.library.add_book(book):
            print("Book added successfully.")
        else:
            print("Failed to add book. ISBN might already exist.")

    def remove_book(self):
        book_id = input("Enter book ID to remove: ")
        if self.library.remove_book(book_id):
            print("Book removed successfully.")
        else:
            print("Failed to remove book. Book ID might not exist.")

    def list_books(self):
        books = self.library.list_books()
        if books:
            for book in books:
                print(f"ID: {book.id}, {book}")
        else:
            print("No books in the library.")

    def search_books(self):
        keyword = input("Enter search keyword: ")
        books = self.library.search_books(keyword)
        if books:
            for book in books:
                print(f"ID: {book.id}, {book}")
        else:
            print("No books found.")

    def borrow_book(self):
        book_id = input("Enter book ID to borrow: ")
        if self.library.borrow_book(book_id):
            print("Book borrowed successfully.")
        else:
            print("Failed to borrow book. It might not exist or already be borrowed.")

    def return_book(self):
        book_id = input("Enter book ID to return: ")
        if self.library.return_book(book_id):
            print("Book returned successfully.")
        else:
            print("Failed to return book. It might not exist or not be borrowed.")