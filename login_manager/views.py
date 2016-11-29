from pprint import pprint

from requests import HTTPError
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route, api_view

from social.apps.django_app.utils import psa

@api_view(['GET'])
@psa('social:complete')
def register_by_access_token(request, backend):
    """
    This view expects an access_token GET parameter, if it's needed,
    request.backend and request.strategy will be loaded with the current
    backend and strategy.

    http://psa.matiasaguirre.net/docs/use_cases.html#signup-by-oauth-access-token
    :param request:
    :param backend:
    :return:
    """
    token = request.GET.get('access_token')
    if not token:
        return Response('Missing access_token parameter.', status=status.HTTP_400_BAD_REQUEST)
    try:
        user = request.backend.do_auth(request.GET.get('access_token'))
        print user.username
    except HTTPError as ex:
        print (ex.message)
        return Response('Invalid access_token.', status=status.HTTP_403_FORBIDDEN)
    if user:
        return Response('OK')
    else:
        return Response('ERROR', status=status.HTTP_403_FORBIDDEN)