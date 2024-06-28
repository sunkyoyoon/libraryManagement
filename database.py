# database.py

import sqlite3
from models import Book

class Database:
    def __init__(self, db_name='library.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                isbn TEXT UNIQUE,
                is_borrowed INTEGER
            )
        ''')
        self.conn.commit()

    def add_book(self, book):
        try:
            self.cursor.execute('''
                INSERT INTO books (title, author, isbn, is_borrowed)
                VALUES (?, ?, ?, ?)
            ''', (book.title, book.author, book.isbn, int(book.is_borrowed)))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def remove_book(self, book_id):
        self.cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def get_book(self, book_id):
        self.cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
        row = self.cursor.fetchone()
        if row:
            return Book(row[1], row[2], row[3], row[0])
        return None

    def list_books(self):
        self.cursor.execute('SELECT * FROM books')
        return [Book(row[1], row[2], row[3], row[0]) for row in self.cursor.fetchall()]

    def search_books(self, keyword):
        self.cursor.execute('''
            SELECT * FROM books 
            WHERE title LIKE ? OR author LIKE ?
        ''', (f'%{keyword}%', f'%{keyword}%'))
        return [Book(row[1], row[2], row[3], row[0]) for row in self.cursor.fetchall()]

    def update_book(self, book):
        self.cursor.execute('''
            UPDATE books 
            SET title = ?, author = ?, isbn = ?, is_borrowed = ?
            WHERE id = ?
        ''', (book.title, book.author, book.isbn, int(book.is_borrowed), book.id))
        self.conn.commit()
        return True

    def __del__(self):
        self.conn.close()