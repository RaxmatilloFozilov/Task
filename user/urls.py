from django import urls as dj_urls
from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register-or-login/', views.register_or_login, name='register_or_login'),
    path('confirm-email/', views.confirm_email, name='confirm_email'),

]