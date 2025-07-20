from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Book, Library
from django.views.generic.detail import DetailView


def register(request):
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


