from django.http import HttpResponse
from django.conf import settings

import json

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen


def get_places(request, search_term):
    url = 'https://maps.googleapis.com/maps/api/place/queryautocomplete/json?key={0}&input={1}'.format(
        settings.GOOGLE_MAPS_KEY,
        search_term
    )
    response = urlopen(url)
    data = json.loads(response.read())
    return HttpResponse(data, content_type="application/javascript")
