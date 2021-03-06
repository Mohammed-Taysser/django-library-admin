# Generated by Django 3.2 on 2021-04-07 17:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('img', models.ImageField(blank=True, default='photo/default.jpg', upload_to='photo/%Y/%m/%d')),
                ('buy_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('rent_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('status', models.CharField(blank=True, choices=[('available', 'available'), ('rent', 'rent'), ('sold', 'sold')], max_length=50)),
                ('star', models.DecimalField(blank=True, decimal_places=1, max_digits=2)),
                ('added_date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('details', models.TextField(blank=True)),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='library_app.category')),
            ],
        ),
    ]
