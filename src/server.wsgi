import sys, os
sys.path[0:0] = [
    os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            '..',
            'eggs',
            'setuptools-0.6c12dev_r85381-py2.7.egg')
]

from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server
from twitter.routes import dispatcher

def test_application(environ, start_response):
    setup_testing_defaults(environ)
    return dispatcher(environ, start_response)

if __name__ == '__main__':
    make_server('', 8000, test_application).serve_forever()