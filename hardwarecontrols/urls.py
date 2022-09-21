
from django.urls import path, include
from hardwarecontrols.views import (
    HardwareInfoListCreateView,
    HardwareInfoDetailView,
    HardwareSessionListCreateView,
    HardwareSessionDetailView,
    SetCurrentHardwareSessionImageCapture,
    CurrentHardwareSession,
    SessionImageListCreateView,
    SessionImageDetailView
)

urlpatterns = [
    path('info/', HardwareInfoListCreateView.as_view()),
    path('info/<int:id>/', HardwareInfoDetailView.as_view()),
    path('session/', HardwareSessionListCreateView.as_view()),
    path('session/current/', CurrentHardwareSession.as_view()),
    # path('session/current/image_capture/', SetCurrentHardwareSessionImageCapture.as_view()),
    path('session/<int:id>/', HardwareSessionDetailView.as_view()),
    path('session/image/', SessionImageListCreateView.as_view()),
    path('session/image/<int:id>/', SessionImageDetailView.as_view()),
]
