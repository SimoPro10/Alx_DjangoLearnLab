
from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """Query all books by a specific author."""
    try:
        # Get the author object
        author = Author.objects.get(name=author_name)
        # Get all books by this author
        books = Book.objects.filter(author=author)
        
        print(f"Books by {author_name}:")
        for book in books:
            print(f" - {book.title}")
    except Author.DoesNotExist:
        print(f"Author {author_name} does not exist.")

def list_all_books_in_library(library_name):
    """List all books in a library."""
    try:
        # Get the library object
        library = Library.objects.get(name=library_name)
        # Get all books in this library
        books = Book.objects.filter(library=library)
        
        print(f"Books in {library_name}:")
        for book in books:
            print(f" - {book.title}")
    except Library.DoesNotExist:
        print(f"Library {library_name} does not exist.")

def get_librarian_for_library(library_name):
    """Retrieve the librarian for a library."""
    try:
        # Get the library object
        library = Library.objects.get(name=library_name)
        # Get the librarian associated with this library
        librarian = Librarian.objects.get(library=library)
        
        print(f"Librarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library {library_name} does not exist.")
    except Librarian.DoesNotExist:
        print(f"No librarian found for {library_name}.")


