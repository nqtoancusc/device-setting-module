from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from rest_framework import viewsets
from .serializers import SettingSerilizer
from .models import Setting
from django_filters.rest_framework import DjangoFilterBackend
from .forms import SettingForm

# Create your views here.
class SettingsViewset(viewsets.ModelViewSet):
    queryset = Setting.objects.all();
    serializer_class = SettingSerilizer

class SettingViewset(viewsets.ModelViewSet):
    serializer_class = SettingSerilizer
    def get_queryset(self):
        """ allow rest api to filter by device_id """
        queryset = Setting.objects.all();
        device_id = self.request.query_params.get('device_id', None)
        if device_id is not None:
            queryset = queryset.filter(device_id=device_id)
        
        return queryset

def device_setting_list(request):
    device_setting_objects = Setting.objects.all();

    device_id = request.GET.get('device_id');
    if device_id != '' and device_id is not None:
        device_setting_objects = device_setting_objects.filter(device_id__icontains=device_id) # To search by exact keyword, use device_id__icontains=device_id

    # Each page render 10 records
    paginator = Paginator(device_setting_objects,10)
    page = request.GET.get('page');
    device_setting_objects = paginator.get_page(page)

    return render(request,'html/device_setting_list.html',{'device_setting_objects':device_setting_objects});

def create_device_setting(request):
    form = SettingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/device-settings')

    return render(request,'html/create_device_setting.html',{'form':form})

def update_device_setting(request, id):
    setting = Setting.objects.get(id=id)
    form = SettingForm(request.POST or None, instance=setting)
    if form.is_valid():
        form.save()
        return redirect('/device-settings')

    return render(request,'html/update_device_setting.html',{'form':form, 'setting': setting})