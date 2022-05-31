from django.urls import path
from . import views

urlpatterns =[
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),
    path('search/', views.search, name='search'),
    path('main/', views.main, name='main')
]

