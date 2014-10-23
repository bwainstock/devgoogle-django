from django.shortcuts import render

from tweetstream.models import Tweets

# Create your views here.

def index(request):
	# latest_tweets = Tweets.objects.all().order_by('-created')[:5]
	latest_tweets = Tweets.objects.all().order_by('-created')
	context = {'latest_tweets': latest_tweets}
	return render(request, 'tweets/index.html', context)

def latest(request):
	# latest = Tweets.objects.all().order_by('-created')[:1]
	latest = Tweets.objects.all().order_by('-created')[:5]
	context = {'latest': latest}
	return render(request, 'tweets/latest.html', context)

def tag(request, tag):
	latest_tweets = Tweets.objects.filter(tags__tag=tag)
	context = {'latest_tweets': latest_tweets}
	return render(request, 'tweets/index.html', context)