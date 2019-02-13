# Generated by Django 2.1.2 on 2019-02-13 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=60, verbose_name='Фамилия')),
                ('sex', models.CharField(choices=[('М', 'Мужской'), ('Ж', 'Женский')], max_length=1, verbose_name='Пол')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
            ],
        ),
    ]
