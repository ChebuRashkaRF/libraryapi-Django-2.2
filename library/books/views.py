from django.views.generic import ListView

from .models import Book


class BookListView(ListView):
    """Все книги"""

    model = Book
    template_name = 'bool_list.html'
