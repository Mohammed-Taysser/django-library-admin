from django import forms
from . import models


class AddNewCategory(forms.ModelForm):
	
	class Meta:
		model = models.Category
		fields = ['name']


class AddNewBook(forms.ModelForm):
	class Meta:
		model = models.Book
		fields = '__all__'
		# widgets = {
		# 	'title': forms.TextInput(attrs={'class': 'form-control'}),
		# 	'author': forms.TextInput(attrs={'class': 'form-control'}),
		# 	'img': forms.FileInput(attrs={'class': 'form-control'}),
		# 	'pages': forms.TextInput(attrs={'class': 'form-control'}),
		# 	'buy_price': forms.NumberInput(attrs={'class': 'form-control'}),
		# 	'rent_price': forms.NumberInput(attrs={'class': 'form-control'}),
		# 	'rent_date': forms.TextInput(attrs={'class': 'form-control'}),
		# 	'active': forms.CheckboxInput(attrs={'class': 'form-control'}),
		# 	'status': forms.Select(attrs={'class': 'form-control'}),
		# 	'category': forms.Select(attrs={'class': 'form-control'}),
		# 	'star': forms.NumberInput(attrs={'class': 'form-control'}),
		# 	'star_rate': forms.NumberInput(attrs={'class': 'form-control'}),
		# 	'date_create': forms.DateInput(attrs={'class': 'form-control'}),
		# }
