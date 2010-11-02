import unittest
from twitter import Twitter, User

unittest.TestLoader.testMethodPrefix = "should_"

class TwitterTests(unittest.TestCase):

    def setUp(self):
        self.twitter = Twitter()

    def should_allow_user_to_post_tweet(self):
        self.twitter.tweet('user', 'message')
        self.assertEqual([{'user':'user', 'message':'message'}], list(self.twitter.timeline()))

    def should_limit_tweets_to_140_chars(self):
        self.assertRaises(ValueError, self.twitter.tweet, 'user', 'x' * 141)

    def should_show_latest_tweets_most_recent_first_when_unauthenticated(self):
        self.twitter.tweet('user1', 'hello')
        self.twitter.tweet('user2', 'world')
        self.assertEqual([{'user':'user2', 'message':'world'},
                          {'user':'user1', 'message':'hello'}],
                         list(self.twitter.timeline()))

    def should_limit_timeline_to_last_10_tweets(self):
        for i in range(11):
            self.twitter.tweet('user', str(i))
        self.assertEqual([{'user':'user', 'message':'10'}, {'user':'user', 'message':'9'},
                          {'user':'user', 'message':'8'}, {'user':'user', 'message':'7'},
                          {'user':'user', 'message':'6'}, {'user':'user', 'message':'5'},
                          {'user':'user', 'message':'4'}, {'user':'user', 'message':'3'},
                          {'user':'user', 'message':'2'}, {'user':'user', 'message':'1'},],
                         list(self.twitter.timeline()))

class TwitterUserTests(unittest.TestCase):

    def setUp(self):
        self.twitter = Twitter()
        self.user = User(name='matt', twitter=self.twitter)
        self.steve = User(name='steve')
        self.user.follow(self.steve)

    def should_allow_users_to_follow_other_users(self):
        self.assertEqual([self.steve], self.user.followed_tweeters)

    def should_limit_timeline_to_followed_tweeters_tweets(self):
        self.twitter.tweet(self.steve, 'hello there')
        self.twitter.tweet('someone else', 'hi')
        self.twitter.tweet(self.steve, 'hello again')
        self.assertEqual([{'user':self.steve, 'message':'hello again'},
                          {'user':self.steve, 'message':'hello there'},
                          ], list(self.user.timeline))

    def should_limit_timeline_10_tweets_from_followed_users(self):
        carl = User(name='Carl')
        self.user.follow(carl)

        for i in range(11):
            self.twitter.tweet(self.steve, str(i))
            self.twitter.tweet(carl, str(i))
            self.twitter.tweet('asf', str(i))

        self.assertEqual([{'user':carl, 'message':'10'},
                          {'user':self.steve, 'message':'10'},
                          {'user':carl, 'message':'9'},
                          {'user':self.steve, 'message':'9'},
                          {'user':carl, 'message':'8'},
                          {'user':self.steve, 'message':'8'},
                          {'user':carl, 'message':'7'},
                          {'user':self.steve, 'message':'7'},
                          {'user':carl, 'message':'6'},
                          {'user':self.steve, 'message':'6'},
                         ],
                        list(self.user.timeline))

if __name__ == '__main__':
    unittest.main()