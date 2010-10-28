from django.forms.models import ModelForm
from picoblog.models import Timeline, Tweeter

class TimelineForm(ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(TimelineForm, self).__init__(*args, **kwargs)
        self.user = user

    def save(self, *args, **kwargs):
        new_model = super(TimelineForm, self).save(commit=False)
        new_model.user = self.user
        new_model.save()

    class Meta:
        model = Timeline
        exclude = ('user', )


class FollowTweetersForm(ModelForm):

    class Meta:
        model = Tweeter
        exclude = ('user', )