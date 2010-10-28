from django.db import models
from django.contrib.auth.models import User

class Timeline(models.Model):
    user = models.ForeignKey(User)
    message = models.CharField(max_length=60)
    update_timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.message

    @staticmethod
    def get_recent_updates(user=None):
        if user:
            queryset = Timeline.objects.filter(
                user__in=(list(user.get_profile().followed_tweeters.all()) + [user]))
        else:
            queryset = Timeline.objects.all()
        return queryset.order_by('-update_timestamp')[0:5]

class Tweeter(models.Model):
    user = models.ForeignKey(User)
    followed_tweeters = models.ManyToManyField(User, related_name='followed_tweeters', blank=True)

    def follow(self, user):
        self.followed_tweeters.add(user)