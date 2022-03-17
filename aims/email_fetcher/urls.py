from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('mailbox/', views.mailbox_view, name='mailbox'),
    path('inventory/', views.inventory_view, name='inventory')
]