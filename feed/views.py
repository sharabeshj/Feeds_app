from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login,authenticate
from django.contrib.auth.models import User as auth_user
from .models import Feed
import datetime
# Create your views here

def index(request):
	return render(request,'feed/basic.html',{'title':'Feeds'})

def login(request):
	if request.method == "POST":
		print("hi")
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				auth_login(request,user)
				u = auth_user()
				name = u.get_username()
				now = datetime.datetime.now()
				text = "%s has joined the network" %name
				p = Feed(user=name,time=now,content = name)
				p.save()
				return redirect('/')
	else:
		print("hi")
		return render(request,'registration/login.html',{'title':'Login'})

