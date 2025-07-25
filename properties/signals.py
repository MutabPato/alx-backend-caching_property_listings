from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Property
from django.core.cache import cache


@receiver([post_save, post_delete], sender=Property)
def invalidate_property_cache(sender, instance, **kwargs):
    cache.delete('all_properties')