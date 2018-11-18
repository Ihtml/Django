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
	article = models.Article.objects.get(pk=1)
	return render(request, 'blog/index.html', {'article': article})
		



