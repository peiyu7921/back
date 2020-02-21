from requests import Response
from rest_framework_jwt.settings import api_settings
from rest_framework.authentication import (
    get_authorization_header
)
from django.utils.encoding import smart_text
from rest_framework import exceptions
import time
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER

class MyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # response['X-My-Header'] = "my value"
        # print(self.get_jwt_value(request))
        try:
            payload = jwt_decode_handler(self.get_jwt_value(request))
            currentTime = int(time.time())
            if payload['exp'] - currentTime < 82800:
                response.data['refreshToken'] = True
                # you need to change private attribute `_is_render`
                # to call render second time
                response._is_rendered = False
                response.render()
        except BaseException as e:
            # print(e)
            pass
        return response

    def get_jwt_value(self, request):
        auth = get_authorization_header(request).split()
        auth_header_prefix = api_settings.JWT_AUTH_HEADER_PREFIX.lower()

        if not auth:
            if api_settings.JWT_AUTH_COOKIE:
                return request.COOKIES.get(api_settings.JWT_AUTH_COOKIE)
            return None

        if smart_text(auth[0].lower()) != auth_header_prefix:
            return None

        if len(auth) == 1:
            msg = _('Invalid Authorization header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid Authorization header. Credentials string '
                    'should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        return auth[1]