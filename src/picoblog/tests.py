from django import test
from django.core.urlresolvers import reverse as reverse_url
from django.contrib.auth.models import User
from picoblog.models import Timeline, Tweeter

class TestPicoblogAcceptance(test.TestCase):

    def setUp(self):
        self.client = test.Client()
        self.client.login(username="matt", password="asdf")
        user = User.objects.get(pk=1)
        for i in range(6):
            Timeline.objects.create(user=user, message="Message %s" % i)

    def should_show_all_recent_tweets_on_homepage(self):
        client = test.Client()
        response = client.get(reverse_url('picoblog:main'))
        self.assertEqual(5, len(response.context['timeline']))
        self.assertEqual(Timeline.objects.all().order_by('-update_timestamp')[0],
                         response.context['timeline'][0])

    def should_show_timeline_of_5_most_recent_tweets(self):
        response = self.client.get(reverse_url('picoblog:main'))
        self.assertEqual(5, len(response.context['timeline']))
        self.assertEqual(Timeline.objects.all().order_by('-update_timestamp')[0],
                         response.context['timeline'][0])

    def should_let_user_add_messages(self):
        self.client.login(username="matt", password="asdf")
        response = self.client.post(reverse_url('picoblog:main'),
                         {'message':'Hello picoblog readers'}, follow=True)
        self.assertEqual(200, response.status_code)

    def should_not_show_tweets_of_non_followed_tweeters(self):
        user = User.objects.create(username="sarah")
        Tweeter.objects.create(user=user)
        Timeline.objects.create(user=user, message='first post')
        response = self.client.get(reverse_url('picoblog:main'))
        for message in response.context['timeline']:
            self.assertNotEqual('first post', message.message)

class TestFollowerAcceptance(test.TestCase):

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.other_users = [User.objects.get(pk=2),
                            User.objects.get(pk=3)]
        self.client = test.Client()
        self.client.login(username="matt", password="asdf")

    def should_allow_user_to_follow_other_users(self):
        response = self.client.get(reverse_url('picoblog:follow'), follow=True)
        self.assertEqual([self.other_users[0]], list(response.context['followed_tweeters']))
