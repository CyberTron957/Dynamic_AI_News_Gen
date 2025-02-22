import re
from .models import URLModel

class PageViewMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Only track GET requests
        if request.method == 'GET':
            path = request.path.strip('/')
            
            # Exclude certain paths
            if path and (path.startswith('area/') or path.startswith('article/')):
                # Get or create the URL record
                url_obj, created = URLModel.objects.get_or_create(path=path)
                # Set is_article to True if path starts with 'article/'
                if path.startswith('article/'):
                    url_obj.is_article = True
                # Increment visits
                url_obj.visits += 1
                url_obj.save()
        return response