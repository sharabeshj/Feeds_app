from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from jsonfield import JSONField
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User,primary_key = True,on_delete = models.CASCADE)
	
@receiver(post_save,sender = User)
def create_user_profile(sender,instance,created,**kwrags):
	if created:
		Profile.objects.create(user = instance)

@receiver(post_save,sender = User)
def save_user_profile(sender,instance,**kwargs):
	instance.profile.save()	


class Activity(models.Model):
	LIKE = 'L'
	COMMENT = 'C'
	ACTIVITY_TYPES = (
		(LIKE,'Like'),
		(COMMENT,'Comment'))
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	activity_type = models.CharField(max_length = 1,choices = ACTIVITY_TYPES)
	article = models.CharField(max_length = 30)
	time = models.DateTimeField()

class Article(models.Model):
	profile = models.ForeignKey(Profile,related_name = 'posted_by',on_delete = models.CASCADE)
	content = models.TextField()
	name = models.CharField(max_length = 50,primary_key = True)	
	time = models.DateTimeField()
	like = models.IntegerField(default = 0)
	comment = models.IntegerField(default = 0)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('article-detail',args = [self.name])

	def get_likers(self):
		likers = Activity.objects.all().filter(activity_type = 'L',article = self.name)
		return likers


class Form(models.Model):
	name = models.CharField(max_length= 50)
	article = models.TextField()

