from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', Login),
    path('autenticacion/', Autenticacion),
    path('logout/', Logout),
    path('index/', Index),
    path('register/', Register)
]
