import os

from django.conf import settings
from models import Tweets

from twython import TwythonStreamer


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devgoogle.settings")

class Streamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
			tweet_text = data['text'].encode('utf-8')
			user = data['user']['screen_name'].encode('utf-8')
			created = data['created_at'].encode('utf-8')
            
			t = Tweets(tweet_text=tweet_text, user=user, 
				created=created)
			t.save()

    def on_error(self, status_code, data):
        print status_code
