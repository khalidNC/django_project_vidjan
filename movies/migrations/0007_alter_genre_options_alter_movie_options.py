# Generated by Django 4.2 on 2024-02-06 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_alter_movie_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ('title',)},
        ),
    ]
