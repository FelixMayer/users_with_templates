from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('form_submit', views.form_submit),
    path('user_delete', views.user_delete),
]