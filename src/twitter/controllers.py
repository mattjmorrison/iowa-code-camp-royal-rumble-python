from twitter.models import Twitter

def index(request):
    twitter = Twitter()
    twitter.tweet("asdf", "hi")
    return {'tweets': twitter.timeline()}

def sample_data_dump(request):
    return {'name':'Matt', 'status':'awesome',}