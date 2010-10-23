from django import test
import mock
from picoblog.models import Picoblog

class PicoblogTests(test.TestCase):

    @mock.patch('picoblog.models.Picoblog.objects')
    def should_allow_users_to_post_messages(self, picoblog_mock):
        Picoblog.post_message("Matt", "Hello")
        self.assertEqual(((), {'user':'Matt', 'message':'Hello'}),
                         picoblog_mock.create.call_args)

