from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author_name = "Author Name"
Author.objects.get(name=author_name)


# 2. List all books in a specific library
library_name = "Main Library"

library = Library.objects.get(name=library_name)
books_in_library = library.books.all()  
    
# 3. Retrieve the librarian for a specific library

librarian = Librarian.objects.get(library=library)
   