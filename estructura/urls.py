from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_register', views.new_register, name='new_register'),
    path('list/', views.list, name='list'),
    path('details/<int:id>', views.details, name='details'),
    path('delete/<int:id>', views.delete, name='delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
