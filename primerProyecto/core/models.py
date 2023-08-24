from django.db import models


class Book:
    def __init__(self, isbn, title, year):
        self.isbn = isbn
        self.title = title
        self.year = year


class Library:
    def __init__(self) -> None:
        b1 = Book("a001", "The Catcher in the Rye", 1951)
        b2 = Book("a002", "The Grapes of Wrath", 1939)
        self.book_list = [b1, b2]

    def add_book(self,book):