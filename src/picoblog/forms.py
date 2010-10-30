from django.forms.models import ModelForm
from picoblog.models import Timeline, Tweeter
from django.contrib.auth.models import User

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

    def __init__(self, *args, **kwargs):
        super(FollowTweetersForm, self).__init__(*args, **kwargs)
        queryset = User.objects.exclude(pk=self.instance.pk)
        self.fields['followed_tweeters'].queryset = queryset

    class Meta:
        model = Tweeter
        exclude = ('user', )