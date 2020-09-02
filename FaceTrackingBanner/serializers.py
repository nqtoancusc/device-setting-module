from rest_framework import serializers
from .models import Setting

class SettingSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = ['id','created','updated','device_id','threshold_yaw','threshold_pitch','threshold_roll'];