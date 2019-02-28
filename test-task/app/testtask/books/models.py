from django.db import models
from authors.models import Author

# Create your models here.
class Book(models.Model):
    title = models.CharField(
        'Title',
        max_length=120,
        unique_for_year='pub_date'
    )
    pub_date = models.DateField('Date of publication')
    genre = models.CharField('Genre', max_length=60)
    isbn = models.CharField(
        'ISBN code',
        max_length=250,
        unique=True
    )
    authors = models.ManyToManyField(Author, related_name='author')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('pub_date', 'title',)