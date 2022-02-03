from django.core.cache import cache
from django.conf import settings

from ..models import ZebraUsers
def get_user_accounts():
    import pdb
    if "all_user_accounts" in cache:
        all_user_account = cache.get("all_user_accounts")
        
        
    else:
        all_user_account = ZebraUsers.objects.only("primary_form_firstname","primary_form_lastname", "primary_form_username", "primary_form_role","access_facility_id","access_facility_location")
        pdb.set_trace()
        cache.set("all_user_accounts",all_user_account,timeout=settings.CACHE_TIME_OUT)
        
    user_count = all_user_account.count()
        
    return user_count
    # user_count = all_user_account.count()
    # pdb.set_trace()
    
    # pass