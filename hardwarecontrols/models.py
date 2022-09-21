from django.db import models
from prediction.models import Disease


class HardwareInfo(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False)
    total_time = models.FloatField(default=0)
    motor_run_time = models.FloatField(default=0)
    water_motor_run_time = models.FloatField(default=0)
    is_process_started = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.id} - {self.name}'


class HardwareSession(models.Model):
    hardware_info = models.ForeignKey(HardwareInfo, null=True, on_delete=models.SET_NULL)
    total_images_captured = models.IntegerField(default=0)
    total_healthy_images = models.IntegerField(default=0)
    total_diseased_images = models.IntegerField(default=0)
    is_current_session = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    is_image_capture = models.BooleanField(default=False) 
    is_session_cancelled = models.BooleanField(default=False)
    datetime = models.DateTimeField (auto_now= True, blank = True, null=True)

    def __str__(self) -> str:
        return f'{self.id} - current session: {self.is_current_session} - completion : {self.is_completed}'


class SessionImage(models.Model):
    hardware_session = models.ForeignKey(HardwareSession, on_delete=models.CASCADE)
    disease_name = models.ForeignKey(Disease, blank=True, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='hardware_images')
    is_healthy = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.hardware_session} - healthy: {self.is_healthy}'

