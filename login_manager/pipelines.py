from pprint import pprint

from requests import request, HTTPError

from django.core.files.base import ContentFile


def save_profile_picture(backend, user, response, *args, **kwargs):
    """
    """
    print response
    print backend.name

    if backend.name == 'facebook':
        print response.get('gender')
        pass
    # https://developers.facebook.com/docs/facebook-login/permissions
    # http://psa.matiasaguirre.net/docs/pipeline.html
