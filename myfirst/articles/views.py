from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from django.urls import reverse

from articles.models import Article, Comment

def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})

def detail(request, article_id):
    try:
        a = Article.objects.get( id = article_id )
    except:
        raise Http404("Статья не найдена лол")

    latest_articles_list = a.comment_set.order_by('-id')[:10]
    return render(request, 'articles/detail.html', {'article': a, 'latest_articles_list': latest_articles_list})



    return HttpResponseRedirect(reverse('articles:detail', args = (a.id,)) )
def test(request, comment_id):

    a = Comment.objects.get( id = comment_id )
    a.comment_text=request.POST['text']
    a.save()

    return HttpResponseRedirect(reverse('articles:detaill', args =  (a.id,)) )

def detaill(request, comment_id):


    a = Article.objects.get( id = 1)
    latest_articles_list = a.comment_set.order_by('-id')[:10]
    return render(request, 'articles/detail.html', {'article': a, 'latest_articles_list': latest_articles_list})

def fan(request, comment_id):
    try:
        a =  Comment.objects.get( id = comment_id )
    except:
        raise Http404("Статья не найдена")
    return render(request, 'articles/redact.html', {'comment': a})

def del_comment(request, comment_id):
    a = Comment.objects.get( id = comment_id )
    a.delete()
    a = '1'

    return HttpResponseRedirect(reverse('articles:detaill', args =  (a)) )

def leave_comment(request, article_id):
    try:
        a = Article.objects.get( id = article_id )
    except:
        raise Http404("Статья не найдена")

    a.comment_set.create(authorn_name = request.POST['name'], comment_text = request.POST['text'])


    return HttpResponseRedirect( reverse('articles:detail', args = (a.id,)) )
