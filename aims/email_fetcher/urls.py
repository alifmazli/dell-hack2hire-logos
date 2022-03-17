from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboardView, name='index'),
    # path('login/', views.loginView, name='login')
]