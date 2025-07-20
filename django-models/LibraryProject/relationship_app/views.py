from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.http import HttpResponseForbidden
from .models import Book, Library, UserProfile, Author
from django.views.generic.detail import DetailView
from django import forms


def user_register(request):
    """Handle user registration."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book-list')  # Redirect to book list after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


@login_required
def list_books(request):
    """Retrieves all books and renders a template displaying the list."""
    books = Book.objects.all() #Fetching all book instances from the db
    context = {'book_list': books} #Creating a context dictionary to store all the books from db
    return render(request, 'relationship_app/list_books.html', context) 


class LibraryDetailView(DetailView):
    """Displays the details of a specific library and lists all books in that library."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get books associated with this library through the many-to-many relationship
        context['book_list'] = self.object.books.all()
        return context


# Role-based access control functions
def is_admin(user):
    """Check if user has Admin role."""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'


def is_librarian(user):
    """Check if user has Librarian role."""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'


def is_member(user):
    """Check if user has Member role."""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# Role-based views
@user_passes_test(is_admin)
def admin_view(request):
    """View accessible only to users with Admin role."""
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian)
def librarian_view(request):
    """View accessible only to users with Librarian role."""
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member)
def member_view(request):
    """View accessible only to users with Member role."""
    return render(request, 'relationship_app/member_view.html')


# Book Form for adding and editing books
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']


# Permission-enforced views for book operations
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    """Add a new book (requires 'can_add_book' permission)."""
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = BookForm()
    
    return render(request, 'relationship_app/book_form.html', {
        'form': form,
        'action': 'Add',
        'title': 'Add New Book'
    })


@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    """Edit an existing book (requires 'can_change_book' permission)."""
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = BookForm(instance=book)
    
    return render(request, 'relationship_app/book_form.html', {
        'form': form,
        'action': 'Edit',
        'title': f'Edit Book: {book.title}'
    })


@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    """Delete a book (requires 'can_delete_book' permission)."""
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        book.delete()
        return redirect('book-list')
    
    return render(request, 'relationship_app/book_confirm_delete.html', {
        'book': book
    })