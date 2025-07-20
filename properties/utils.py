from django.core.cache import cache
from .models import Property
import json
from django.core.serializers import serialize
from django_redis import get_redis_connection
import logging

logger = logging.getLogger(__name__)

def get_all_properties():
    data = cache.get('all_properties')
    if data is None:
        queryset = Property.objects.all()
        data = serialize('json', queryset)
        cache.set('all_properties', data, 3600)
    try:
        return json.loads(data)
    except:
        cache.delete('all_properties')
        queryset = Property.objects.all()
        data = serialize('json', queryset)
        cache.set('all_properties', data, 3600)
        return json.loads(data)

def get_redis_cache_metrics():
    conn = get_redis_connection("default")
    info = conn.info("stats")
    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)
    total_requests = hits + misses

    if total_requests > 0:
        hit_ratio = hits / total_requests
        logger.info(f"'hits': {hits}, 'misses': {misses}, 'hit_ratio': {hit_ratio}")
        return {"hits": hits, "misses": misses, "hit_ratio": hit_ratio}
    else:
        hit_ratio = 0
        logger.error("No requests made to the redis database")
        return {"hits": hits, "misses": misses, "hit_ratio": hit_ratio}




