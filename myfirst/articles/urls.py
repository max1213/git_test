from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:article_id>/', views.detail, name = 'detail'),
    path('<int:comment_id>/del_comment', views.del_comment, name = 'del_comment'),
    path('<int:article_id>/leave_comment', views.leave_comment, name = 'leave_comment'),
    path('<int:comment_id>/test', views.test, name = 'test'),
    path('<int:comment_id>/fan', views.fan, name = 'fan'),
    path('<int:comment_id>/detaill', views.detaill, name = 'detaill'),
    

]
