from django.conf.urls import url
from django.urls import path
from . import views
from django.views.generic import ListView,DetailView
from article.models import Article

urlpatterns = [
	url(r'^$',ListView.as_view(queryset = Article.objects.all().order_by('-time'),template_name = "article/articleList.html"),{'title':'Article'}),
	url(r'/(?P<pk>[-\w ]+)',views.ArticleDetailView.as_view(),name = 'article-detail')]