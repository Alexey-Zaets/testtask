# Generated by Django 2.1.2 on 2019-02-13 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ('last_name',)},
        ),
    ]
