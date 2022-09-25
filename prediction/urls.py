
from django.urls import path, include
from prediction.views import (
    ReportList, 
    RawImageList, 
    ReportDetail, 
    RawImageDetailView, 
    RawImageListCreateView, 
    ReportMobileList, 
    ReportMobileDetail
)

urlpatterns = [
    # path('images/', ImageList.as_view()),
    path('images/', RawImageList.as_view()),
    path('images/mobile/<int:id>/', RawImageDetailView.as_view()),
    path('images/mobile/', RawImageListCreateView.as_view()),
    path('reports/', ReportList.as_view()),
    path('reports/<int:id>/', ReportDetail.as_view()),
    path('reports/mobile/', ReportMobileList.as_view()), 
    path('reports/mobile/<int:id>/', ReportMobileDetail.as_view()),
]
