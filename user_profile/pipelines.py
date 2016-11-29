from requests import request, HTTPError

from django.core.files.base import ContentFile

from .models import Profile


def add_gamer_user(backend, user, response, *args, **kwargs):
    """
    Fill users profile with social information.
    """

    print (response)
    print (backend.name)
    print ('add_gamer_user')
    print (user)
    print (hasattr(user, 'profile'))
    # if not backend.name == 'facebook'
    if not hasattr(user, 'profile'):
        profile = dict()

        age_range = response.get('age_range')
        # Determine if the user is an adult according to the response.
        if not age_range:
            profile['adult'] = False
        elif age_range.has_key('min') and age_range['min'] in [18, 21]:
            profile['adult'] = True
        elif age_range.has_key('max') and age_range['max'] == 20:
            profile['adult'] = True
        else:
            profile['adult'] = False

        profile['profile_pict'] = response.get('picture', dict()).get('data', dict()).get('url')

        Profile.objects.create(user=user, **profile)