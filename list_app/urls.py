from django.urls import path
from .views import RegisterViews,DashboardViews
from . import views
urlpatterns = [
    path('register/',RegisterViews.as_view() , name='register'),
    path('',  DashboardViews.as_view() , name='dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add, name='add'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    path('complete/<int:todo_id>/', views.complete, name='complete'),
    path('edit/<int:id>/', views.edit, name='edit'),
]