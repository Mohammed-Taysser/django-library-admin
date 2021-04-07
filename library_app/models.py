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
	pages = models.IntegerField(blank=True)
	buy_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
	rent_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
	rent_date = models.IntegerField(blank=True)
	active = models.BooleanField(default=True)
	status = models.CharField(max_length=50, blank=True, choices=[('available', 'available'), ('rent', 'rent'), ('sold', 'sold')])
	category = models.ForeignKey(Category, on_delete= models.PROTECT, blank=True)
	star = models.DecimalField(decimal_places=1, max_digits=2)
	star_rate = models.IntegerField()
	date_update = models.DateTimeField(auto_now=True)
	date_create = models.DateTimeField(default=timezone.now)
	details = models.TextField(blank=True)
	
	def __str__(self):
		return self.title
