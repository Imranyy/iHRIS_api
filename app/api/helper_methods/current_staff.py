
from django.core.cache import cache
from django.conf import settings

from ..models import ZebraCurrentStaff,ZebraStaffRegistered
def get_curent_staff():
    
    if "current_staff" in cache:
        current_staff = cache.get("current_staff")
    else:
        current_staff = ZebraCurrentStaff.objects.only("person_firstname", "demographic_gender","cadre_name","county_name","ward_district_name","field_currentage","field_hire_year", "field_retirement_date")
        cache.set("current_staff",current_staff, timeout=settings.CACHE_TIME_OUT)
        
    all_current_staff = current_staff.count()
    all_current_staff = "{:,}".format(all_current_staff)
    print("------------------>>>> get_curent_staff")
    return all_current_staff
from datetime import date
def get_registered_staff():
    if "registered_staff" in cache:
        registered_staff = cache.get("registered_staff")
    else:
        registered_staff = ZebraStaffRegistered.objects.all()
        # only("person_firstname","person_nationality","demographic_gender","registration_council","facility_location")
        cache.set("registered_staff",registered_staff, timeout=settings.CACHE_TIME_OUT)
    todays_date = date.today()
    current_year = todays_date.year
    currently_registered = []
    for staff in registered_staff:
        import pdb
        print("==========>>>>>>>>>>>>>>>>>>>",int(staff.registration_license_expiration.strftime('%Y')))
        if int(staff.registration_license_expiration.strftime('%Y')) >= int(current_year):
            print("----------- ############", staff.registration_license_expiration)
            currently_registered.append(staff.registration_license_expiration.strftime('%Y'))
            
    count_currently_registered = len(currently_registered)
    
    registered_staff = "{:,}".format(count_currently_registered)
    print("------------------>>>> get_registered_staff")
    return registered_staff