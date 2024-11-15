from django.db import models

class Profile(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    alt_username = models.JSONField(default=list, blank=True, null=True)
    total_media = models.IntegerField(default=0)
    total_photo = models.IntegerField(default=0)
    total_video = models.IntegerField(default=0)
    profile_view = models.IntegerField(default=0)
    display_name = models.CharField(max_length=100, blank=True, null=True)
    # other fields, like bio, profile picture, etc.

    def __str__(self):
        return self.username
    


