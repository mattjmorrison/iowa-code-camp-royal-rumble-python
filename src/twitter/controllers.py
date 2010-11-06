from twitter.models import Twitter
from pesto import Response

twitter = Twitter()

def index(request):
    return {'tweets': twitter.timeline()}

def new_message(request):
    twitter.tweet(request['name'], request['message'])
    return Response.redirect("/")

def tweet_data(request):
    return {'tweets': twitter.timeline()}