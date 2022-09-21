
from django.urls import path, include

urlpatterns = [
    path('prediction/', include('prediction.urls')),
    path('hardware/', include('hardwarecontrols.urls')),
]
