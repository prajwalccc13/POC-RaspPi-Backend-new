from django.contrib import admin
from .models import RawImage, Cure, Disease, Report

admin.site.register(RawImage)
admin.site.register(Cure)
admin.site.register(Disease)
admin.site.register(Report)