import uuid

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return f"{self.title} has been borrowed."
        return f"{self.title} is already borrowed."

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return f"{self.title} has been returned."
        return f"{self.title} was not borrowed."


class Member:
    def __init__(self, name):
        self.name = name
        self.member_id = uuid.uuid4()
        self.borrowed_books = []

    def borrow_book(self, book: Book):
        if not book.is_borrowed:
            book.borrow()
            self.borrowed_books.append(book)
            return f"{self.name} borrowed {book.title}"
        return f"{book.title} is not available"

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return f"{self.name} returned {book.title}"
        return f"{self.name} doesn't have {book.title}"


class Librarian:
    def __init__(self, name):
        self.name = name
        self.librarian_id = uuid.uuid4()

    def add_book(self, library, book: Book):
        library.books.append(book)
        return f"Librarian {self.name} added {book.title}"


class Library:
    def __init__(self):
        self.library_id = uuid.uuid4()
        self.books = []
        self.members = []

    def register_member(self, member: Member):
        self.members.append(member)
        return f"Registered member: {member.name}"


# Demonstration
if __name__ == "__main__":
    library = Library()
    librarian = Librarian("Sarah")
    book1 = Book("1984", "George Orwell", "123456")
    book2 = Book("Python Basics", "John Doe", "654321")
    member = Member("Mobeen")

    print(librarian.add_book(library, book1))
    print(librarian.add_book(library, book2))
    print(library.register_member(member))

    print(member.borrow_book(book1))
    print(member.return_book(book1))
