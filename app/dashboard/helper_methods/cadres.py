from django.core.cache import cache
from django.conf import settings

from ..models import ZebraCurrentStaff,ZebraAllStaff
def get_count_by_cadres():
    """Function that gets cadres count
    Args:
        county(str): ...
    Returns:
        response(dict): all cadres count
    """
    if "current_staff" in cache:
        current_staff = cache.get("current_staff")
    else:
        current_staff = ZebraCurrentStaff.objects.only("person_firstname", "demographic_gender","cadre_name","county_name","ward_district_name","field_currentage","field_hire_year", "field_retirement_date")
        cache.set("current_staff",current_staff, timeout=settings.CACHE_TIME_OUT)
        
    all_available_cadres = {}
    cadre_counter = 0
    for staff in current_staff:
        if staff.cadre_name not in all_available_cadres:
            all_available_cadres[staff.cadre_name] = cadre_counter
        else:
            all_available_cadres[staff.cadre_name] = all_available_cadres[staff.cadre_name]+1
    print("----------->>>>> ",all_available_cadres)
    return all_available_cadres

from datetime import date
def get_count_retiring():
    """Function that fetch count of all retiring staff
    Args:
        org_unit(str): queries for each org_unit
    Returns:
        response(int): all schedules
    """
    todays_date = date.today()
    current_year = todays_date.year
    retiring_staff_count = []
    import pdb
    
    if "current_staff" in cache:
        current_staff = cache.get("current_staff")
    else:
        current_staff = ZebraCurrentStaff.objects.only("person_firstname", "demographic_gender","cadre_name","county_name","ward_district_name","field_currentage","field_hire_year", "field_retirement_date")
        cache.set("current_staff",current_staff, timeout=settings.CACHE_TIME_OUT)
    
    for staff in current_staff:
        if staff.field_retirement_date is not None and staff.field_retirement_date.strftime('%Y')== str(current_year):
            retiring_staff_count.append(staff.field_retirement_date)
            # retirement_date = staff.field_retirement_date
            # retiriment_year = retirement_date.strftime('%Y')
        
            # if retiriment_year == str(current_year):
            #     retiring_staff_count.append(retiriment_year)
    retirement_count = len(retiring_staff_count)        
    retirement_count = "{:,}".format(retirement_count)    
    print("============>>>>>>>>>> retiring_this_year")
    return retirement_count