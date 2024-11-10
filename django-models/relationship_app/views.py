from dbm.ndbm import library
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book,Library
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile
from .forms import BookForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required



def book_list(request):
     
      books = Book.objects.all() 
      context = {'books': books}  
      return render(request, 'relationship_app/book_list.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all() 
        return context

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
]

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
]






def is_admin(user):
    return user.userprofile.role == 'admin'

def is_librarian(user):
    return user.userprofile.role == 'librarian'

def is_member(user):
    return user.userprofile.role == 'member'


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')


@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')


@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to the list of books
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

# View to edit a book (requires 'can_change_book' permission)
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to the list of books
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

# View to delete a book (requires 'can_delete_book' permission)
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to the list of books
    return render(request, 'delete_book.html', {'book': book})