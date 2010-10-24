from django import test
import mock
from tweeter.models import Tweeter
from django.contrib.auth.models import User

class TweeterTests(test.TestCase):

    def should_get_tweeter_from_django_user_profile(self):
        self.assertRaises(Tweeter.DoesNotExist, User().get_profile)

    def should_allow_tweeters_to_follow_other_tweeters(self):
        tweeter_one = Tweeter()
        tweeter_two = Tweeter()
        with mock.patch('tweeter.models.Tweeter.followed_tweeters') as follow_mock:
            tweeter_one.follow(tweeter_two)
            self.assertEqual(((tweeter_two,), {}), follow_mock.add.call_args)

    