from django.contrib import admin

# Register your models here.
from feed.models import Feed
from article.models import Article,Profile,Activity

admin.site.register(Feed)
admin.site.register(Article)
admin.site.register(Profile)
admin.site.register(Activity)