import logging
from django.http import JsonResponse

logger = logging.getLogger(__name__)

class AccessLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.path.startswith('/auth/'):  # Example for protected paths
            logger.info(f"User {request.user.username} accessed {request.path}")
        return self.get_response(request)

class ErrorHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except Exception as e:
            logger.error(f"Server error: {str(e)}")
            return JsonResponse({'error': 'Server Error'}, status=500)
        if response.status_code == 404:
            return JsonResponse({'error': 'Page Not Found'}, status=404)
        return response
