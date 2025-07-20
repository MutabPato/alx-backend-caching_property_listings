from django.shortcuts import render
from .models import Property
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from .utils import get_all_properties

@cache_page(60 * 15)
def property_list(request):
    """
    View to return all properties as json.
    """
    data = get_all_properties()
    return JsonResponse({'properties': data})
