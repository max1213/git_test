from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from articles.models import Article, Comment

def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})

def detail(request, article_id):
    try:
        a = Article.objects.get( id = article_id )
    except:
        raise Http404("Статья не найдена")

    latest_articles_list = a.comment_set.order_by('-id')[:10]
    return render(request, 'articles/detail.html', {'article': a, 'latest_articles_list': latest_articles_list})

def leave_comment(request, article_id):
    try:
        a = Article.objects.get( id = article_id )
    except:
        raise Http404("Статья не найдена")

    a.comment_set.create(authorn_name = request.POST['name'], comment_text = request.POST['text'])


    return HttpResponseRedirect( reverse('articles:detail', args = (a.id,)) )

def redact_comment(request, article_id):
    try:
        с = Article.objects.get( id = article_id )
    except:
        raise Http404("Статья не найдена")

    a = Comment.objects.get( id = request.POST['name'] )

    a.comment_text=request.POST['text']
    a.save()

    return HttpResponseRedirect( reverse('articles:detail', args = (с.id,)) )

def del_comment(request, article_id):
    try:
        с = Article.objects.get( id = article_id )
    except:
        raise Http404("Статья не найдена")

    a = Comment.objects.get( id = request.POST['name'] )

    a.delete()


    return HttpResponseRedirect( reverse('articles:detail', args = (с.id,)) )
