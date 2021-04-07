from django.shortcuts import render
from . import models

# Create your views here.


def dashboard(request):
	db_books_objects = models.Book.objects.all()
	db_category_objects = models.Category.objects.all()
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
	db_category_objects = models.Category.objects.all()
	data = {
		'page_name': 'update book'.title(),
		'db_category_objects': db_category_objects,
	}
	return render(request, 'library_app/pages/update_book.html', data)


def book_detail(request, book_id):
	db_category_objects = models.Category.objects.all()
	data = {
		'page_name': 'book detail'.title(),
		'db_category_objects': db_category_objects,
	}
	return render(request, 'library_app/pages/books_details.html', data)

