#!/usr/bin/env python3

class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        """Return all contracts for this author"""
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        """Return all books this author has contracts for"""
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Create a new contract linking this author to a book"""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Return total royalties across all contracts"""
        return sum(contract.royalties for contract in self.contracts())


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        """Return all contracts for this book"""
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """Return all authors who have contracts for this book"""
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        # Validate types
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        if not isinstance(book, Book):
            raise Exception("book must be a Book instance")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts signed on a specific date"""
        return [contract for contract in cls.all if contract.date == date]
