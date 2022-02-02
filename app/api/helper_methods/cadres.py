from django.core.cache import cache

from ..models import ZebraCurrentStaff,ZebraAllStaff
def get_count_by_cadres():
    if "current_staff" in cache:
        current_staff = cache.get("current_staff")
    else:
        current_staff = ZebraCurrentStaff.objects.only("person_firstname", "demographic_gender","cadre_name","county_name","ward_district_name","field_currentage","field_hire_year", "field_retirement_date")
        cache.set("current_staff",current_staff, timeout=360000)
        
    all_available_cadres = {}
    cadre_counter = 0
    for staff in current_staff:
        if staff.cadre_name not in all_available_cadres:
            all_available_cadres[staff.cadre_name] = cadre_counter
        else:
            all_available_cadres[staff.cadre_name] = all_available_cadres[staff.cadre_name]+1
    return all_available_cadres

from datetime import date
def get_count_retiring():
    todays_date = date.today()
    current_year = todays_date.year
    retiring_staff_count = []
    current_staff = ZebraCurrentStaff.objects.only("field_retirement_date")
    for staff in current_staff:
        # print(datetime.datetime.now())
        if staff.field_retirement_date is not None:
            retirement_date = staff.field_retirement_date
            retiriment_year = retirement_date.strftime('%Y')
        
            if retiriment_year == current_year:
                retiring_staff_count.append(retiriment_year)
    retirement_count = len(retiring_staff_count)            
    import pdb
    pdb.set_trace()
    pass