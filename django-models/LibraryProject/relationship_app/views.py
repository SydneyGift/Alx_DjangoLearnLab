from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic import DetailView

def book_list(request):
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
        context['book_list'] = Book.objects.filter(library=self.object)
        return context
