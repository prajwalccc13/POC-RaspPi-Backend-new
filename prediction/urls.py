
from django.urls import path, include
from prediction.views import ReportList, RawImageList, ReportDetail

urlpatterns = [
    # path('images/', ImageList.as_view()),
    path('images/', RawImageList.as_view()),
    path('reports/', ReportList.as_view()),
    path('reports/<int:id>/', ReportDetail.as_view()),
]
