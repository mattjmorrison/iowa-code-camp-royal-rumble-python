import mock
from django import test
from picoblog.models import Tweeter
from django.contrib.auth.models import User

class TweeterTests(test.TestCase):

    def should_get_tweeter_from_django_user_profile(self):
        self.assertRaises(Tweeter.DoesNotExist, User().get_profile)

    @mock.patch('picoblog.models.Tweeter.followed_tweeters')
    def should_allow_tweeters_to_follow_other_tweeters(self, follow_mock):
        tweeter = Tweeter()
        Tweeter().follow(tweeter)
        self.assertEqual(((tweeter,), {}), follow_mock.add.call_args)

    @mock.patch('picoblog.models.Picoblog.objects')
    def should_allow_tweeters_to_add_messages_to_timeline(self, picoblog_mock):
        tweeter = Tweeter()
        tweeter.post_message("sample message")
        self.assertEqual(((), {'user':tweeter, 'message':'sample message'}),
                         picoblog_mock.create.call_args)

    @mock.patch('picoblog.models.Picoblog.objects.filter')
    def should_retrieve_all_tweets_for_tweeter(self, timeline_filter):
        timeline_filter.return_value = []
        tweeter = Tweeter()
        self.assertEqual([], tweeter.posts())
        self.assertEqual(((), {'tweeter':tweeter}), timeline_filter.call_args)

    @mock.patch('picoblog.models.Picoblog.objects.filter')
    @mock.patch('picoblog.models.Q')
    def should_retrieve_all_tweets_for_a_tweeters_followers(self, q_mock, filter_mock):
        filter_mock.return_value = []
        q_mock.return_value = q_mock

        tweeter = Tweeter.objects.create(user=User.objects.create(username='x'))
        t2 = Tweeter.objects.create(user=User.objects.create(username='y'))
        tweeter.followed_tweeters.add(t2)

        self.assertEqual([], tweeter.followers_tweets())
        self.assertEqual(((q_mock,), {}), filter_mock.call_args)

        self.assertEqual(((), {'tweeter':t2}), q_mock.call_args)
        
        