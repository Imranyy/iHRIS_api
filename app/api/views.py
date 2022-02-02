from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from django.core.cache import cache

from .models import ZebraCurrentStaff
import pandas as pd

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
def home(request):
    # all_current_staff = ZebraCurrentStaff.objects.all().count()
    
    # cadre_table = get_count_by_cadres()
    retiring_next_year = get_count_retiring()
    context = {
    #    "all_current_staff": "{:,}".format(all_current_staff), 
    #    "cadre_table" : cadre_table
    }
    return render(request,'dashboard/dash_content.html', context)