from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

class Picoblog(models.Model):
    tweeter = models.ForeignKey('Tweeter')
    @staticmethod
    def post_message(user, message):
        Picoblog.objects.create(user=user, message=message)

class Tweeter(models.Model):
    user = models.ForeignKey(User, unique=True)
    followed_tweeters = models.ManyToManyField('Tweeter')

    def follow(self, tweeter):
        self.followed_tweeters.add(tweeter)

    def post_message(self, message):
        Picoblog.post_message(self, message)

    def posts(self):
        return Picoblog.objects.filter(tweeter=self)

    def followers_tweets(self):
        criteria = None
        for tweeter in self.followed_tweeters.all():
            criteria = Q(tweeter=tweeter)

        return Picoblog.objects.filter(criteria)
