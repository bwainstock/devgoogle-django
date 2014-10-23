from django.db import models

from nltk.corpus import stopwords

# Create your models here.
class Tweets(models.Model):
	tweet_text = models.CharField(max_length=145)
	created = models.DateTimeField('Tweeted on')
	user = models.CharField(max_length=20)
	real_name = models.TextField()
	profile_image_url = models.TextField()

	def __unicode__(self):
		return self.tweet_text

	def google_string(self):
		words = self.tweet_text.split()
		for i, word in enumerate(words):
			if "#" in word:
				words.pop(i)
		return '+'.join(words)

	def get_tags(self):
		tag_list = []
		
		for tweet_tag in self.tags_set.all():
			if tweet_tag.tag not in stopwords.words('english'):
				tag_list.append(tweet_tag.tag)
		return tag_list


class Tags(models.Model):
	tag = models.CharField(max_length=140)
	tweet = models.ManyToManyField(Tweets)

	def __unicode__(self):
		return self.tag