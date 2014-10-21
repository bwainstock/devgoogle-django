from django.shortcuts import render

from tweetstream.models import Tweets

# Create your views here.

def index(request):
	latest_tweets = Tweets.objects.all().order_by('-created')[:5]
	context = {'latest_tweets': latest_tweets}
	return render(request, 'tweets/index.html', context)