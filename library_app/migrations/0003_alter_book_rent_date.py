# Generated by Django 3.2 on 2021-04-07 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0002_alter_book_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rent_date',
            field=models.IntegerField(blank=True),
        ),
    ]
