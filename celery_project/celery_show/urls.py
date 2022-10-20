
from django.urls import path,include
from .views import show
urlpatterns = [
    path('', show , name = "show"),
]
