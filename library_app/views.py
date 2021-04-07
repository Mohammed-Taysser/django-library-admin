from django.shortcuts import render, get_object_or_404, redirect
from . import models
from . import forms

# Create your views here.


def dashboard(request):
	db_books_objects = models.Book.objects.all()#.values('id','author', 'title', 'buy_price', 'rent_price', 'img', 'status')
	db_category_objects = models.Category.objects.all()
	if request.method == 'POST':
		form_set = forms.AddNewCategory(request.POST)
		if form_set.is_valid():
			form_set.save()
	data = {
		'page_name': 'dashboard'.title(),
		'db_books_objects': db_books_objects,
		'db_category_objects': db_category_objects,
	}
	return render(request, 'library_app/pages/dashboard.html', data)


def delete_book(request, book_id):
	db_category_objects = models.Category.objects.all()
	data = {
		'page_name': 'delete book'.title(),
		'db_category_objects': db_category_objects,
	}
	return render(request, 'library_app/pages/delete_book.html', data)


def update_book(request, book_id):
	current_book = get_object_or_404(models.Book, id=book_id)
	db_category_objects = models.Category.objects.all()
	if request.method == 'POST':
		form_set = forms.AddNewBook(request.POST, request.FILES, instance=current_book)
		if form_set.is_valid():
			form_set.save()
			return redirect('/')
	else:
		form_set = forms.AddNewBook(instance=current_book)
	data = {
		'page_name': 'update book'.title(),
		'db_category_objects': db_category_objects,
		'form_set': form_set
	}
	return render(request, 'library_app/pages/update_book.html', data)


def book_detail(request, book_id):
	db_category_objects = models.Category.objects.all()
	current_book = get_object_or_404(models.Book, id=book_id)
	data = {
		'page_name': current_book.title.title(),
		'db_category_objects': db_category_objects,
		'current_book': current_book,
	}
	return render(request, 'library_app/pages/books_details.html', data)


def add_book(request):
	db_category_objects = models.Category.objects.all()
	if request.method == 'POST':
		form_set = forms.AddNewBook(request.POST, request.FILES)
		if form_set.is_valid():
			form_set.save()
			return redirect('/')
	data = {
		'page_name': 'delete book'.title(),
		'db_category_objects': db_category_objects,
	}
	return render(request, 'library_app/pages/new_book.html', data)
