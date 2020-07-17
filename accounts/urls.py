from django.urls import path
from .views import accounts, register, login, profile

urlpatterns = [
    path('', accounts, name='accounts'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile')
]