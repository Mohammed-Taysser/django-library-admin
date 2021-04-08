from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=50)
	
	def __str__(self):
		return self.name


class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	img = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True,  default='photo/default.jpg')
	buy_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
	rent_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
	rent_day = models.IntegerField(default=1, blank=True)
	status = models.CharField(max_length=50, blank=True, choices=[('available', 'available'), ('rent', 'rent'), ('sold', 'sold')])
	category = models.ForeignKey(Category, on_delete= models.PROTECT, blank=True, default='none')
	star = models.DecimalField(decimal_places=1, max_digits=2, blank=True, default=0)
	added_date = models.DateField(default=timezone.now, blank=True)
	details = models.TextField(blank=True)
	
	def __str__(self):
		return self.title
