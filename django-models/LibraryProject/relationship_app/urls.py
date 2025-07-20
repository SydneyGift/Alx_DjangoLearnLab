"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # URL for listing all books
    path('books/', views.list_books, name='book-list'),
    # URL for viewing a specific library by its primary key (ID)
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
    # Authentication URLs
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.user_register, name='register'),
    
    # Role-based URLs
    path('admin-view/', views.admin_view, name='admin-view'),
    path('librarian-view/', views.librarian_view, name='librarian-view'),
    path('member-view/', views.member_view, name='member-view'),
    
    # Permission-enforced book operation URLs
    path('books/add/', views.add_book, name='add-book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit-book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete-book'),
]