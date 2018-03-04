from django.db import models

# Create your models here.

class Feed(models.Model):
	user = models.CharField(max_length=50)
	time = models.DateTimeField()
	content = models.TextField()
	like = models.IntegerField(null=True,blank=True)
	comment = models.TextField(null=True,blank=True)

	def __str__(self):
		return self.user

	class Meta:
		ordering = ["time"]
	
