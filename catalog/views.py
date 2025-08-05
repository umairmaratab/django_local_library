from django.shortcuts import render

# Create your views here.
from .models import Author, Book, BookInstance, Genre


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact="a").count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    genres_particular_word = Genre.objects.filter(name__contains="help").count()
    book_particular_word = Book.objects.filter(title__contains="eat").count()

    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
        "books_with_particular_word": book_particular_word,
        "genre_with_particular_word": genres_particular_word,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html", context=context)
