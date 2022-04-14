from django.urls import path
from . import views

urlpatterns = [
    path('', views.BurgerList.as_view()),
]