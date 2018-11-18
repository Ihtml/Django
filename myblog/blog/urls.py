from django.urls import path
from . import views

# 命名空间
app_name = 'blog'
urlpatterns = [
	# ex: /blog/
	path('', views.index, name='index'),
]
