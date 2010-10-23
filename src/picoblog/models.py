from django.db import models

class Picoblog(models.Model):
    @staticmethod
    def post_message(user, message):
        Picoblog.objects.create(user=user, message=message)
