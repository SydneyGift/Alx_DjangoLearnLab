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
from .views import list_books, LibraryDetailView, user_login, user_logout, user_register


urlpatterns = [
    path('admin/', admin.site.urls),
    # URL for listing all books
    path('books/', list_books, name='book-list'),
    # URL for viewing a specific library by its primary key (ID)
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    # Authentication URLs
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register')
]
