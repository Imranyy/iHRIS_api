
from ..models import ZebraCurrentStaff
def get_curent_staff():
    all_current_staff = ZebraCurrentStaff.objects.all().count()
    all_current_staff = "{:,}".format(all_current_staff)
    return all_current_staff