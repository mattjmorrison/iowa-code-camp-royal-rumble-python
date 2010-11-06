class Twitter(object):

    def __init__(self):
        self._tweets = []

    def tweet(self, user, message):
        if len(message) > 140:
            raise ValueError("Message is too long")
        self._tweets.append({'user':user, 'message':message})

    def timeline(self):
        return list(reversed(self._tweets[-10:]))

    def limit_timeline_to_users(self, tweeters):
        tweet_count = 0
        for tweet in reversed(self._tweets):
            if tweet_count >= 10:
                raise StopIteration

            if tweet['user'] in tweeters:
                tweet_count += 1
                yield tweet

class User(object):

    def __init__(self, name, twitter=None):
        self.name = name
        self.twitter = twitter
        self._followed_tweeters = []

    def follow(self, user):
        self._followed_tweeters.append(user)

    @property
    def followed_tweeters(self):
        return self._followed_tweeters

    @property
    def timeline(self):
        return self.twitter.limit_timeline_to_users(self.followed_tweeters)