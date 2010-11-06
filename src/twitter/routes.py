from pesto import dispatcher_app
from twitter import controllers
from twitter.templates import to_html, to_json

dispatcher = dispatcher_app()

dispatcher.match('/',
                 GET=controllers.index,
                 decorators=[to_html('index.html')])

dispatcher.match('/post', POST=controllers.new_message)

dispatcher.match('/data',
                 GET=controllers.tweet_data,
                 decorators=[to_html('sample.html')])

dispatcher.match('/data/json',
                 GET=controllers.tweet_data,
                 decorators=[to_json])

