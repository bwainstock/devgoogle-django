from django.contrib import admin
from tweetstream.models import Tweets, Tags


admin.site.register(Tweets)
admin.site.register(Tags)