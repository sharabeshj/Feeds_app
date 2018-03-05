from django.conf.urls import url
from . import views
from django.views.generic import ListView
from article.models import Article

urlpatterns = [
	url(r'^$',ListView.as_view(queryset = Article.objects.all(),template_name = "article/article.html"),{'title':'Article'})]