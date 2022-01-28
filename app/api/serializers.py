from rest_framework import serializers
from .models import ZebraCurrentStaff

class CurrentStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZebraCurrentStaff
        fields = ("person_firstname", "demographic_gender","cadre_name")