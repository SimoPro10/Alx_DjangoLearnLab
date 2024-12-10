<<<<<<< HEAD
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    
    def __str__(self):
        return f"{self.user.username} - {self.role}"
    
@receiver(post_save, sender=User)
def created_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
    

class Author(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name    
    
class Book(models.Model):
    title = models.CharField(max_length=50)
    # author is a Foreign key from the author model and can be accessed from the author model as books
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
    def __str__(self):
        return self.title     
    
    class Meta:
        permissions = [
            ('can_add_book', 'Can add book'),
            ('can_change_book', 'can change book'),
            ('can_delete_book', 'can delete book')
        ]
    
# Library Model:
# name: CharField.
# books: ManyToManyField to Book.

class Library(models.Model):
    name = models.CharField(max_length=50)
    # books has a ManytoMany rel. to the Library model and can be accessed from the book model as libraries_found
    books = models.ManyToManyField(Book, related_name='Libraries_found')
    

    def display_books(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(book.title for book in self.books.all()[:3])

    display_books.short_description = 'Books'

    def display_book_count(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return len(self.books.all())

    display_book_count.short_description = 'Count of Books'
    
    def __str__(self):
        return self.name    

# Librarian Model:
# name: CharField.
# library: OneToOneField to Library.

class Librarian(models.Model):
    name = models.CharField(max_length=50)
    # library has a OnetoOne rel. to the Librarian model and can be accessed from the Library model as libraries_found
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='Librarian')
=======
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
    
    def __str__(self):
        return f"{self.title} by {self.author}"  

#Extending Book Model with Custom Permissions
    class Meta(models.Model):
        Permissions_Choices =(
            ('can_add_book', 'can_add_book'),
            ('can_change_book', 'can_change_book'),
            ('can_delete_book', 'can_delete_book'),

        )
    permissions = models.CharField(max_length=50,  choices='Permissions_Choices')
    meta = models.TextField()
    
    def __str__(self):
        return f'{self.user.username} - {self.permissions}'

class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name   

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarians')

    def __str__(self):
        return self.name
    
#Extending User Model with a UserProfile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    Role_Choices =(
        ('Admin','Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    
    )

role = models.CharField(max_length=50,  choices='Role_Choices')
userprofile = models.TextField()

def __str__(self):
    return f'{self.user.username} - {self.role}'

#Signal to automatically create a UserProfile when a new User is created
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
>>>>>>> 16dee7aeb905a470e30d02d3bea5cea76272bc25
