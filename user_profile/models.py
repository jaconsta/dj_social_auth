from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Profile (models.Model):
    """
    Manage the user profile, and additionals to provided by default Django user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Some social networks do not provide the exact age but an approximation.
    # And adult is considered to be >18 years old.
    adult = models.BooleanField(default=False)

    # The avatar picture
    profile_pict = models.URLField()
