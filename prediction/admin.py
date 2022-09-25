from django.contrib import admin
from .models import RawImage, Cure, Disease, Report, RawImageMobile, ReportMobile

admin.site.register(RawImage)
admin.site.register(Cure)
admin.site.register(Disease)
admin.site.register(Report)
admin.site.register(RawImageMobile)
admin.site.register(ReportMobile)