from django.db import models
from django.utils import timezone

# Create your models here.
class Setting(models.Model):
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField()
    device_id = models.IntegerField()
    threshold_yaw = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    threshold_pitch = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    threshold_roll = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(Setting, self).save(*args, **kwargs)

class Device(models.Model):
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)
    setting_id = models.IntegerField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    count = models.IntegerField()