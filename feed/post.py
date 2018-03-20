#!/usr/bin/python
# -*- coding: <UTF-8> -*-


from django import forms
from django.forms import ModelForm
from article.models import Form

class Post(ModelForm):
    class Meta:
    	model = Form
    	fields = ['name','article']

	
			