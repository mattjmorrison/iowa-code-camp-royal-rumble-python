from django import test
import mock
from picoblog.models import Tweeter
from django.contrib.auth.models import User

class TweeterTests(test.TestCase):

    def should_get_tweeter_from_django_user_profile(self):
        self.assertRaises(Tweeter.DoesNotExist, User().get_profile)

    def should_allow_tweeters_to_follow_other_tweeters(self):
        tweeter_one = Tweeter()
        tweeter_two = Tweeter()
        with mock.patch('picoblog.models.Tweeter.followed_tweeters') as follow_mock:
            tweeter_one.follow(tweeter_two)
            self.assertEqual(((tweeter_two,), {}), follow_mock.add.call_args)

    @mock.patch('picoblog.models.Picoblog.objects')
    def should_allow_tweeters_to_add_messages_to_timeline(self, picoblog_mock):
        tweeter = Tweeter()
        tweeter.post_message("sample message")
        self.assertEqual(((), {'user':tweeter, 'message':'sample message'}),
                         picoblog_mock.create.call_args)

