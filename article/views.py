from django.shortcuts import render
from article.models import Article
from django.views.generic.detail import DetailView
from .models import Article

# Create your views here.
class ArticleDetailView(DetailView):
	model = Article
	
	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = self.object.name
		return context	

