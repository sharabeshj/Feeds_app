from django import forms

class Post(forms.Form):
    name = forms.CharField(label='Article name', max_length=50)
    article = forms.CharField(label = 'Your article',max_length=400)