# logger(level='DEBUG', reqeuest_type='GET', url='', status_code='', message=None)
from .utils import logger


class RequestLogHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # log request/response information
        logger(level='INFO',
               reqeuest_type=request.method,
               url=request.build_absolute_uri(),
               status_code=response.status_code,
               message='')

        return response
