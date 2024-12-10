from django.contrib import admin
from .models import Book
<<<<<<< HEAD

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')
=======
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
>>>>>>> 16dee7aeb905a470e30d02d3bea5cea76272bc25

admin.site.register(Book, BookAdmin)