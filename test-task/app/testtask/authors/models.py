from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField('Имя', max_length=60)
    last_name = models.CharField('Фамилия', max_length=60)
    sex = models.CharField(
        'Пол',
        max_length=1,
        choices=(('М', 'Мужской'),('Ж', 'Женский'))
    )
    birthday = models.DateField('Дата рождения')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        ordering = ('last_name',)