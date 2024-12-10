<<<<<<< HEAD
# CRUD Operations - Create: 

## Command Instruction: 
Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949.

## Code : 
`>>> a_book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)`

## Expected output:
`>>> 
#*A new empty prompt signifies a successful creation*`
=======
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()
>>>>>>> 16dee7aeb905a470e30d02d3bea5cea76272bc25
