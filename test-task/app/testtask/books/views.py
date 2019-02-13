from rest_framework import viewsets
from django_filters import rest_framework as filters
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('pub_date', 'title')
