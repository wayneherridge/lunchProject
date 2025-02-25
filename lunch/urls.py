from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create/', views.lunch_create_view, name='lunch_create'),
    path('list/', views.lunch_list_view, name='lunch_list'),
    path('update/<int:lunch_id>/', views.lunch_update_view, name='lunch_update'),
    path('delete/<int:lunch_id>/', views.lunch_delete_view, name='lunch_delete'),
]