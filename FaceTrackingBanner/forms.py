from django import forms
from .models import Setting

class SettingForm(forms.ModelForm):
    class Meta:
        model = Setting
        fields = ['device_id', 'threshold_yaw', 'threshold_pitch', 'threshold_roll']