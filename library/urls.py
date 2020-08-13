from django.urls import path

from library import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('books/', views.search, name='books'),
    path('books/<int:pk>/', views.book, name='book'),
    path('books/<int:pk>/reserve/', views.reserve, name='reserve'),
    path('faq/', views.faq, name='faq'),
    path('users/<str:username>/', views.profile, name='profile'),
    path('check-due-dates/', views.check_due_dates, name='check_due_dates'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('notifications/', views.notifications, name='notifications'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/find/', views.find_user, name='find_user'),
    path('dashboard/authors/add/', views.add_author, name="add_author"),
    path('dashboard/categories/add/', views.add_category, name='add_category'),
    path('dashboard/defaulters/', views.defaulters, name='defaulters'),
    path('dashboard/books/', views.search, name='books_staff'),
    path('dashboard/books/add/', views.add_book, name='add_book'),
    path('dashboard/books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('dashboard/books/<int:pk>/delete/', views.delete_book,
         name='delete_book'),
    path('dashboard/history/<int:pk>/view/', views.history, name='history'),
    path('dashboard/history/<int:pk>/update/', views.update, name='update'),
]
