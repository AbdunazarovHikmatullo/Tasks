from django.urls import path
from .views import register, login_view
from django.contrib.auth import logout

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout, name='logout')
]
