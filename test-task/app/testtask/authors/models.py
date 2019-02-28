from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField('First name', max_length=60)
    last_name = models.CharField('Last name', max_length=60)
    sex = models.CharField(
        'Sex',
        max_length=1,
        choices=(('M', 'Man'),('W', 'Woman'))
    )
    birthday = models.DateField('Birthday')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        ordering = ('last_name',)