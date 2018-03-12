from django.db import models

# Create your models here.

class Feed(models.Model):
	user = models.CharField(max_length=50)
	time = models.DateTimeField()
	method = models.CharField(max_length = 50,null = True, blank = True)
	content = models.TextField()

	def __str__(self):
		return self.user

