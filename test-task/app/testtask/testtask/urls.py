"""testtask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from rest_framework import renderers, routers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view
from authors.views import AuthorViewSet, AuthorBooks
from books.views import BookViewSet


author_list = AuthorViewSet.as_view({
    'get': 'list',
    })

author_detail = AuthorViewSet.as_view({
    'get': 'retrieve',
    })

book_list = BookViewSet.as_view({
    'get': 'list',
    })

book_detail = BookViewSet.as_view({
    'get': 'retrieve',
    })

schema_view = get_schema_view(title='Library API')

urlpatterns = [
    path('', schema_view),
    path('admin/', admin.site.urls),
]

urlpatterns += format_suffix_patterns([
    path('books/', book_list, name='book_list'),
    path('authors/', author_list, name='author_list'),
    path('books/<int:pk>/', book_detail, name='book_detail'),
    path('authors/<int:pk>/', author_detail, name='author_detail'),
    path('authors/<int:pk>/books/', AuthorBooks.as_view()),
])

