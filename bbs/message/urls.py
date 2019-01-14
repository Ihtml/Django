from django.urls import path
from . import views

app_name = 'message'
urlpatterns = [
    path('index/', views.getform, name='form_index')
]