from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:title>', views.get_entry, name='entry'),
    path('search/', views.search, name='search'),
    path('new_entry/', views.new_entry, name='new_entry'),
    path('edit_page/', views.edit_page, name='edit_page'),
    path('save_page/', views.save_page, name='save_page'),
    path('random/', views.random_page, name='random_page')
]
