from django.db import models
from django.contrib.auth.models import User

class Tweeter(models.Model):
    user = models.ForeignKey(User, unique=True)
    followed_tweeters = models.ManyToManyField('Tweeter')

    def follow(self, tweeter):
        self.followed_tweeters.add(tweeter)