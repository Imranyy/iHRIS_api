from rest_framework import serializers
from .models import ZebraCurrentStaff, ZebraUsers

class CurrentStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZebraCurrentStaff
        fields = ("person_firstname", "demographic_gender","cadre_name")
        
class UserAccounts(serializers.ModelSerializer):
    class Meta:
        model = ZebraUsers
        fields = ("access_facility_location","primary_form_username")