from relationship_app.models import Author, Book, Library, Librarian

<<<<<<< HEAD
#  “List all books in a library.” task

# Assuming library_name
library_name = "Alor library"

# Get the library object
library = Library.objects.get(name=library_name)

# Fetch the titles of books in the specified library
books_in_library = library.books.all()

# Display the book titles
for title in books_in_library:
    print(title)


#  “Query all books by a specific author.” task

author_name = 'Chinwe Achebe'

author = Author.objects.get(name=author_name)

all_book_by_author = Book.objects.filter(author=author)

for book in all_book_by_author:
    print(book)
    
# Retrieve the librarian for a library.

library_name = 'Ogun State Library'

library = Library.objects.get(name=library_name)

the_librarain = Librarian.objects.get(library=library)

print(the_librarain.name)
=======
# Query 1: All books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()  # Access related books via the `related_name` on ForeignKey
    return books

# Query 2: List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()  # Access related books via the `related_name` on ManyToManyField
    return books

# Query 3: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian  # Access the librarian via the `related_name` on OneToOneField
    return librarian
>>>>>>> 16dee7aeb905a470e30d02d3bea5cea76272bc25
