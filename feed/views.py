from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login,authenticate
from .models import Feed
from article.models import Article
from django.contrib.auth.forms import UserCreationForm
import datetime
from .post import Post
# Create your views here

def index(request):
	return render(request,'feed/basic.html',{'title':'Feeds','userData': Feed.objects.all().order_by('-time')})

def login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				auth_login(request,user)
				now = datetime.datetime.now()
				text = "%s has joined the network" %username
				print(text)
				p = Feed(user=username,time=now,content =text)
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
			text = "%s has joined the network" %username
			p = Feed(user=username,time=now,content =text)
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
				username = request.user
				text = "%s has posted an article on %s" %(username,name)
				p = Feed(user=username,time=time,content =text)
				p.save()
				a = Article(name = name, time = time, content = content)
				a.save()
				return redirect('/')

		else:
			form = Post()
			return render (request,'article/post.html',{'form':form,'title':'Post'})

	else:
		return redirect('/login')

