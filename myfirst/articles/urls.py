from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:article_id>/', views.detail, name = 'detail'),
    path('<int:article_id>/leave_comment/', views.leave_comment, name = 'leave_comment'),
    path('<int:article_id>/redact_comment/', views.redact_comment, name = 'redact_comment'),
    path('<int:article_id>/del_comment/', views.del_comment, name = 'del_comment'),
]
