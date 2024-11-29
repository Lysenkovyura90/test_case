import os
import json
from typing import List, Dict, Any


class Book:
    """
    Represents a book with attributes such as book ID, title, author, year of publication, and status.

    Attributes:
        book_id (int): Unique identifier for the book.
        title (str): Title of the book.
        author (str): Author of the book.
        year (int): Year of publication.
        status (bool): Status of the book (True for in stock, False for issued). Default is True.
    """
    def __init__(self, book_id: int, title: str, author: str, year: int, status: bool = True) -> None:
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self):
        return (f"Id: {self.book_id}, "
                f"title: {self.title}, "
                f"author: {self.author}, "
                f"year: {self.year}, "
                f"status: {self.status}")


class Library:
   
    def __init__(self, library_file: str = 'library.json') -> None:
        self.library_file = library_file
        self.books: List[Book] = self.load_books()

    def load_books(self) -> List[Book]:
       
        
        if os.path.exists(self.library_file):
            with open(self.library_file, 'r', encoding='utf-8') as file:
                return [Book(**book) for book in json.load(file)]
        return []

    def save_books(self) -> None:
       
        with open(self.library_file, 'w', encoding='utf-8') as file:
            json.dump([book.__dict__ for book in self.books], file, ensure_ascii=False, indent=4)

    def generate_book_id(self) -> int:
        
        return max((book.book_id for book in self.books), default=0) + 1

    def add_book(self, title: str, author: str, year: int) -> None:
        
        
        book_id = self.generate_book_id()
        new_book = Book(book_id=book_id, title=title, author=author, year=year)
        self.books.append(new_book)
        self.save_books()

        print(f'New book added. Id: {book_id}\n')

    def delete_book(self, book_id: int) -> None:
  
        book_to_delete = next((book for book in self.books if book.book_id == book_id), None)
        if book_to_delete:
            self.books.remove(book_to_delete)
            self.save_books()
            print(f'Book with Id {book_id} deleted\n')
        else:
            print(f'Book with Id {book_id} not found\n')

    def find_books(self, **kwargs) -> list[Book]:

        found_books = self.books
        for key, value in kwargs.items():
            if isinstance(value, str):
                found_books = [book for book in found_books if value.lower() in getattr(book, key, "").lower()]
            else:
                found_books = [book for book in found_books if getattr(book, key) == value]

        return found_books

    def get_all_books(self) -> List[Book]:

        return self.books

    def change_book_status(self, book_id: int, new_status: bool) -> None:

        current_book = next((book for book in self.books if book.book_id == book_id), None)
        if current_book:
            current_book.status = new_status
            self.save_books()
            if new_status is True:
                status_text = 'in stock'
            else:
                status_text = 'has been issued'

            print(f'Book with Id {book_id} changed status to "{status_text}"\n')
        else:
            print(f'Book with Id {book_id} not found\n')