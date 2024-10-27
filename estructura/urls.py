from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_register', views.new_register, name='new_register'),
    path('list/', views.list, name='list'),
    path('details/<int:id>', views.details, name='details'),
]
