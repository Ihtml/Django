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
	articles = models.Article.objects.all()
	return render(request, 'blog/index.html', {'articles': articles})

def article(request, article_id):
	article = models.Article.objects.get(pk=article_id)
	return render(request, 'blog/article.html', {'article': article})
		



