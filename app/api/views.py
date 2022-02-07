from django.shortcuts import render

from django.core.cache import cache

from rest_framework import status
from rest_framework.response import Response

from rest_framework.decorators import api_view


@api_view(['GET'])
def clear_cache(request):
   if request.method == 'GET':
       cache.clear()
       return_message = {
            "message": ('All Caches cleared Successfully')
        }
       return Response(return_message, status=status.HTTP_200_OK)