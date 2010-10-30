from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse as reverse_url
from shortcuts import render_to
from picoblog.models import Timeline
from picoblog.forms import TimelineForm, FollowTweetersForm

def logged_in_home(request, form=None):
    message_form = form or TimelineForm(request.user)
    follow_form = FollowTweetersForm(instance=request.user.get_profile())
    followed_tweeters = request.user.get_profile().followed_tweeters.all()
    timeline = Timeline.get_recent_updates(request.user)

    return {'timeline': timeline,
        'followed_tweeters': followed_tweeters,
        'form':message_form,
        'follow_form':follow_form}

@render_to("picoblog/templates/index.html")
def main(request):
    if request.user.is_authenticated():
        return logged_in_home(request)
    else:
        return {'timeline': Timeline.get_recent_updates() }

@render_to("picoblog/templates/index.html")
def post_message(request):
    form = TimelineForm(request.user, request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_url('picoblog:main'))
    else:
        return logged_in_home(request, form)

def follow(request):
    form = FollowTweetersForm(request.POST, instance=request.user.get_profile())
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_url('picoblog:main'))