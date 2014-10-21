# import os
#import time
import django
from django.conf import settings
from django.utils import timezone
from tweetstream.models import Tweets, Tags

from twython import TwythonStreamer

django.setup()
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devgoogle.settings")

class Streamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
			tweet_text = data['text'].encode('utf-8')
			user = data['user']['screen_name'].encode('utf-8')
			date = data['created_at'].encode('utf-8')
			real_name = data['user']['name'].encode('utf-8')
			profile_image_url = data['user']['profile_image_url'].encode('utf-8')
#			created = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(date,'%a %b %d %H:%M:%S +0000 %Y'))
			created = timezone.now()
            
			t = Tweets(tweet_text=tweet_text, user=user, created=created,
						real_name=real_name, profile_image_url=profile_image_url
						)
			t.save()

			for word in t.tweet_text.split():
				if Tags.objects.filter(tag=word).exists():
					ta = Tags.objects.get(tag=word)
					ta.tweet.add(t)
				else:
					ta = Tags(tag=word)
					ta.save()
					ta.tweet.add(t)

    def on_error(self, status_code, data):
        print status_code

if __name__ == '__main__':
	stream = Streamer(settings.APP_KEY, settings.APP_SECRET,
					settings.OAUTH_TOKEN, settings.OAUTH_TOKEN_SECRET)
	stream.statuses.filter(track='#testbutt')