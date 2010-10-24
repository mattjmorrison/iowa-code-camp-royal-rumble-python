from django.db import models
from django.contrib.auth.models import User

class Picoblog(models.Model):
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
