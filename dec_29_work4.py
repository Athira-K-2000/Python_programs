class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.books_borrowed = []

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def display_books(self):
        print("Available Books:")
        for book in self.books:
            if book.is_available:
                print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}")

    def display_members(self):
        print("Library Members:")
        for member in self.members:
            print(f"Member ID: {member.member_id}, Name: {member.name}")

    def borrowed_book(self, member_id, book_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.book_id == book_id), None)

        if member and book and book.is_available:
            book.is_available = False
            member.books_borrowed.append(book)
            print(f"Book '{book.title}' borrowed by {member.name}.")
        else:
            print("Invalid member ID or book ID, or the book is not available.")

    def return_book(self, member_id, book_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.book_id == book_id), None)

        if member and book and not book.is_available and book in member.books_borrowed:
            book.is_available = True
            member.books_borrowed.remove(book)
            print(f"Book '{book.title}' returned by {member.name}.")
        else:
            print("Invalid member ID or book ID, or the book is not borrowed by the member.")


# Example Usage:
library = Library()

book1 = Book(1, "The Catcher in the Rye", "J.D. Salinger")
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee")

member1 = Member(101, "Alice")
member2 = Member(102, "Bob")

library.add_book(book1)
library.add_book(book2)
library.add_member(member1)
library.add_member(member2)

library.display_books()
library.display_members()

library.borrowed_book(101, 1)
library.borrowed_book(102, 2)

library.display_books()

library.return_book(101, 1)
library.return_book(102, 2)

library.display_books()
