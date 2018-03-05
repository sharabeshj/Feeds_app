from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
	content = models.TextField()
	name = models.CharField(max_length = 50,primary_key = True)
	time = models.DateTimeField()

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('article-detail',kwargs = {'pk':self.pk})