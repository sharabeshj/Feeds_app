from django.conf.urls import url
from . import views
from django.contrib.auth.views import logout

urlpatterns=[
	url(r'^$',views.index,name = 'index'),
<<<<<<< HEAD
	url(r'^login/$',views.login, name = 'login'),
	url(r'^logout/$',logout,name= 'logout'),
	url(r'^register/$',views.register, name = 'register'),
	url(r'^compose/$',views.compose,name = 'compose'),
	url(r'^ajax/articleLike/$',views.articleLike,name = 'article-like')]
=======
	url(r'^login$',views.login, name = 'login'),
	url(r'^logout$',logout,name= 'logout'),
	url(r'^register$',views.register, name = 'register'),
	url(r'^compose$',views.compose,name = 'compose'),
	url(r'^ajax/articleLike$',views.articleLike,name = 'article-like')]
>>>>>>> cf62b7241b864dc3801f66794b327c5c4f3a1dc8
