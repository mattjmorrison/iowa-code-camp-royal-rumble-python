from pesto import dispatcher_app
from twitter import controllers
from twitter.templates import to_html, to_json

dispatcher = dispatcher_app()

dispatcher.match('/',
                 GET=controllers.index,
                 decorators=[to_html('index.html')])

dispatcher.match('/data.json',
                 GET=controllers.sample_data_dump,
                 decorators=[to_json])

dispatcher.match('/data.html',
                 GET=controllers.sample_data_dump,
                 decorators=[to_html('sample.html')])

