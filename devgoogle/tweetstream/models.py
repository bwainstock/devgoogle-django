from django.db import models

# Create your models here.
class Tweets(models.Model):
	tweet_text = models.CharField(max_length=145)
	created = models.DateTimeField('Tweeted on')
	user = models.CharField(max_length=20)
	real_name = models.TextField()
	profile_image_url = models.TextField()

	def __unicode__(self):
		return self.tweet_text

class Tags(models.Model):
	tag = models.CharField(max_length=140)
	tweet = models.ManyToManyField(Tweets)

	def __unicode__(self):
		return self.tag