from django.shortcuts import render

from django.core.cache import cache

from rest_framework import status
from rest_framework.response import Response

from rest_framework.decorators import api_view
from django.conf import settings

from ..dashboard.models import ZebraAllStaff,ZebraCurrentStaff,ZebraUsers
from ..dashboard.serializers import CurrentStaffSerializer, UserAccountsSerializer



@api_view(['GET'])
def clear_cache(request):
   if request.method == 'GET':
       cache.clear()
       return_message = {
            "message": ('All Caches cleared Successfully')
        }
       return Response(return_message, status=status.HTTP_200_OK)
   
   
@api_view(['GET'])
def all_current_staff(request):
   if request.method == 'GET':
      if "current_staff" in cache:
         current_staff = cache.get("current_staff")      
      else:
         current_staff = ZebraCurrentStaff.objects.all()
         cache.set("CurrentStaffSerializer",current_staff, timeout=settings.CACHE_TIME_OUT)

      serializer = CurrentStaffSerializer(current_staff, many=True)
        
   return Response(serializer.data)

@api_view(['GET'])
def user_account(request):
   if request.method == 'GET':
      if "all_user_accounts" in cache:
         all_user_account = cache.get("all_user_accounts")
      else:
         all_user_account = ZebraUsers.objects.all()
         cache.set("all_user_accounts",all_user_account,timeout=settings.CACHE_TIME_OUT)

      serializer = UserAccountsSerializer(all_user_account, many=True)
        
   return Response(serializer.data)

@api_view(['GET'])
def facilities(request):
   if request.method == 'GET':
      if "facilities" in cache:
         all_user_account = cache.get("facilities")
      else:
         all_user_account = ZebraUsers.objects.all()
         cache.set("facilities",all_user_account,timeout=settings.CACHE_TIME_OUT)

      serializer = UserAccountsSerializer(all_user_account, many=True)
        
   return Response(serializer.data)