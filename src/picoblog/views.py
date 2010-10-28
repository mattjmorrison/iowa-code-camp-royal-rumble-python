from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse as reverse_url
from shortcuts import render_to
from picoblog.models import Timeline
from picoblog.forms import TimelineForm, FollowTweetersForm
from django.contrib.auth.models import User

def logged_in_home(request):
    form = TimelineForm(request.user, request.POST or None)
    follow_form = FollowTweetersForm()
    followed_tweeters = request.user.get_profile().followed_tweeters.all()
    timeline = Timeline.get_recent_updates(request.user)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_url('picoblog:main'))
    else:
        return {'timeline': timeline,
            'followed_tweeters': followed_tweeters,
            'form':form,
            'follow_form':follow_form}

@render_to("picoblog/templates/index.html")
def main(request):
    if request.user.is_authenticated():
        return logged_in_home(request)
    else:
        return {'timeline': Timeline.get_recent_updates() }

def follow(request, id):
    user_to_follow = User.objects.get(pk=id)
    request.user.get_profile().follow(user_to_follow)
    return HttpResponseRedirect(reverse_url('picoblog:main'))
