from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_filters import rest_framework as filters
from books.models import Book
from books.serializers import BookSerializer
from .models import Author
from .serializers import AuthorSerializer


# Create your views here.
class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('last_name',)


class AuthorBooks(APIView):

    def get(self, request, format=None, **kwargs):
        author_id = kwargs.get('pk')
        try:
            author = Author.objects.get(id=author_id)
        except Author.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            books = Book.objects.filter(authors=author_id)
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
