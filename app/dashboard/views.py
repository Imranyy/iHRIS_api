from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from django.core.cache import cache

from .models import ZebraCurrentStaff, ZebraUsers
import pandas as pd

from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings

from .serializers import CurrentStaffSerializer, UserAccountsSerializer


def test(request):
    current_staff = ZebraCurrentStaff.objects.only("person_firstname", "demographic_gender","cadre_name","county_name","ward_district_name","field_currentage","field_hire_year", "field_retirement_date")
    records = current_staff.to
    # print(current_staff)
    master_data_frame = pd.DataFrame.from_records(list(current_staff))
    # print(master_data_frame[:5])
    import pdb
    pdb.set_trace()
    # master_data_frame = pd.DataFrame(list(current_staff.values()))
    
from .helper_methods.cadres import get_count_by_cadres,get_count_retiring
from .helper_methods.users import get_user_accounts
from .helper_methods.current_staff import get_curent_staff, get_registered_staff
def home(request):
    
    all_current_staff = get_curent_staff()
    cadre_table = get_count_by_cadres()
    # retiring_this_year = get_count_retiring()
    user_accounts = get_user_accounts()
    registered_staff = get_registered_staff()
    
    
    context = {
       "all_current_staff": all_current_staff, 
       "cadre_table" : cadre_table,
    #    "retiring_this_year" : retiring_this_year,
       "user_accounts" : user_accounts,
       "registered_staff":registered_staff
    }
    return render(request,'dashboard/dash_content.html', context)
 
