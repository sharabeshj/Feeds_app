from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login,authenticate
from .models import Feed
from article.models import Article,Profile,Activity
from django.contrib.auth.forms import UserCreationForm
import datetime
from django.contrib.auth.models import User
from .post import Post
import jsonpickle
import json
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_protect

# Create your views here

def index(request):
	return render(request,'feed/feed.html',{'title':'Feeds','userData': Feed.objects.all().order_by('-time')})

def login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				auth_login(request,user)
				now = datetime.datetime.now()
				method = 'login'
				text = "%s has joined the network" %username
				p = Feed(user=username,time=now,method = method, content =text)
				p.save()
				return redirect('/')
		else:
			return redirect('/register')
	else:
		return render(request,'registration/login.html',{'title':'Login'})


def register(request):
	if request.method == "POST":
		'''print('hi')'''
		form = UserCreationForm(request.POST)

		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username = username, password = password)
			auth_login(request,user)
			now = datetime.datetime.now()
			method = 'login'
			text = "%s has joined the network" %username
			p = Feed(user=username,time=now,method = method, content =text)
			p.save()	
			return redirect('/')
	else:
		form = UserCreationForm()

	context = {'form': form,'title':'Register'}
	return render(request,'registration/register.html',context)

 
def compose(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			form = Post(request.POST)
			if form.is_valid():
				name = form.cleaned_data['name']
				content = form.cleaned_data['article']
				time = datetime.datetime.now()
				method = 'article'
				username = request.user.username
				text = "%s has posted an article on %s" %(username,name)
				p = Feed(user=username,time=time,method = method, content =text)
				p.save()
				user = User.objects.get(id = request.user.id)
				profile = Profile.objects.get(user = user)
				a = Article(profile = profile,name = name, time = time,content = content)
				a.save()
				return redirect('/')

		else:
			form = Post()
			return render (request,'article/post.html',{'form':form,'title':'Post'})

	else:
		return redirect('/login')

@csrf_protect
def articleLike(request):
	article_id = request.POST.get('id')
	article = Article.objects.get(name = article_id)
	like = Activity.objects.filter(user = request.user, activity_type = Activity.LIKE, article = article.name) 
	if like:
		like.delete()
				
	else:
		like = Activity(user = request.user, activity_type = Activity.LIKE, article = article.name,time = datetime.datetime.now())
		like.save()
	return JsonResponse({'status':'ok'})
	