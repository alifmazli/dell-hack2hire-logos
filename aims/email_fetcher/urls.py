from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('upload', views.display_files_view, name='upload'),
]