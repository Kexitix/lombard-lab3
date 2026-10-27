from .models import Article
from django.shortcuts import render, redirect
from django.http import Http404


def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})
