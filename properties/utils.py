from django.core.cache import cache
from .models import Property
import json
from django.core.serializers import serialize


def get_all_properties():
    data = cache.get('all_properties')
    if data is None:
        queryset = Property.objects.all()
        data = serialize('json', queryset)
        cache.set('all_properties', data, 3600)
    return json.loads(data)
