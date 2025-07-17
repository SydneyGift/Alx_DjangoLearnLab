from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author_name = "Author Name"
books_by_author = Book.objects.filter(author__name=author_name)
print(f"Books by {author_name}:")
for book in books_by_author:
    print(book.title)

# 2. List all books in a specific library
library_name = "Main Library"
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()  
    print(f"\nBooks in {library_name}:")
    for book in books_in_library:
        print(book.title)
except Library.DoesNotExist:
    print(f"No library found with name '{library_name}'")

# 3. Retrieve the librarian for a specific library
try:
    librarian = Librarian.objects.get(library=library)
    print(f"\nLibrarian of {library_name}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"No librarian assigned to library '{library_name}'")
