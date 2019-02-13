from rest_framework import serializers
from .models import Book
from authors.serializers import AuthorFullNameSerializer


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorFullNameSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = (
            'id', 'title', 'isbn',
            'pub_date', 'genre', 'authors'
        )