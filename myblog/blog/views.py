from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from . import models
from django.utils import timezone

# Create your views here.
# use common templates.


def index(request):
	# 倒序获得文章列表
	articles = models.Article.objects.order_by('-id')
	return render(request, 'blog/index.html', {'articles': articles})

def article(request, article_id):
	article = models.Article.objects.get(pk=article_id)
	return render(request, 'blog/article.html', {'article': article})
		
def edit(request, article_id):
	if str(article_id) == '0':
		# 新增
		return render(request, 'blog/edit.html')
	article = models.Article.objects.get(pk=article_id)
		# 编辑
	return render(request, 'blog/edit.html', {'article': article})

def edit_action(request):
	title = request.POST.get('title', 'TITLE')
	content = request.POST.get('content', 'CONTENT')
	models.Article.objects.create(title=title, content=content)
	articles = models.Article.objects.all()
	return render(request, 'blog/index.html', {'articles': articles})