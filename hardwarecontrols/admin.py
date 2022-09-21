from django.contrib import admin
from .models import (
    HardwareInfo,
    HardwareSession,
    SessionImage
)


admin.site.register(HardwareInfo)
admin.site.register(HardwareSession)
admin.site.register(SessionImage)