from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboardView, name='index'),
    path('login/', views.loginView, name='login'),
    path('register/', views.registerView, name='register')
]