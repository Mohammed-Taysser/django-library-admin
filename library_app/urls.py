from django.urls import path
from . import views

app_name = 'library_app'

urlpatterns = [
	path('', views.dashboard, name='dashboard'),
	path('book-detail/<int:book_id>', views.book_detail, name='book-detail'),
	path('update-book/<int:book_id>', views.update_book, name='update-book'),
	path('delete-book/<int:book_id>', views.delete_book, name='delete-book'),
]
