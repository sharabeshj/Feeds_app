from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login,authenticate
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
				now = datetime.datetime.now()
				text = "%s has joined the network" %username
				print(text)
				p = Feed(user=username,time=now,content =text)
				p.save()
				return redirect('/')
	else:
		print("hi")
		return render(request,'registration/login.html',{'title':'Login'})

