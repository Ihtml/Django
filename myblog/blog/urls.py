from django.urls import path
from . import views

# 命名空间
app_name = 'blog'
urlpatterns = [
	# ex: /blog/
	path('index/', views.index, name='index'),
	path('article/<int:article_id>/', views.article, name='article'),
]
