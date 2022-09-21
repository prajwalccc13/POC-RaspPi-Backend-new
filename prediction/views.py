from prediction.utils import predict_disease
from .apps import PredictionConfig

from prediction.models import RawImage, Report, Disease, RawImageMobile, ReportMobile
from prediction.serializers import (
    RawImageSerializer, 
    ReportSerializer
)
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics, permissions


'''
https://medium.com/saarthi-ai/deploying-a-machine-learning-model-using-django-part-1-6c7de05c8d7
'''


class ImageList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = RawImage.objects.all()
    serializer_class = RawImageSerializer


class RawImageList(APIView):
    '''
    Save image for prediction
    '''
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        images = RawImage.objects.all()
        serializer = RawImageSerializer(images, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        user = request.user
        data = request.data

        # print(request)
        # print('----------------------------------')
        # print(request.data)
        # print('++++++++++++++++++++++++')
        # print(next(request.FILES.values()))
        # print('++++++++++++++++++++++++')
        

        try:
            test = next(request.FILES.values())
            raw_image = RawImage(
                user=user,
                # image=data['image']
                image=test
            )
            raw_image.save()

            img_path = raw_image.image.path

            # result = PredictionConfig.predict_disease(img_path=img_path)
            result = predict_disease(img_path=img_path)
            print(result)

            disease = Disease.objects.get(name=result)
            report = Report(
                user= user,
                raw_image= raw_image,
                disease= disease,
            )
            report.save()

            serializer = ReportSerializer(report)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(e, status=status.HTTP_400_BAD_REQUEST)



class RawImageMobileList(APIView):
    '''
    Save image for prediction
    '''
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        images = RawImage.objects.all()
        serializer = RawImageSerializer(images, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data

        try:
            raw_image = RawImage(
                user=user,
                image=data['image']
            )
            raw_image.save()

            img_path = raw_image.image.path

            # result = PredictionConfig.predict_disease(img_path=img_path)
            result = predict_disease(img_path=img_path)
            print(result)

            disease = Disease.objects.get(name=result)
            report = Report(
                user= user,
                raw_image= raw_image,
                disease= disease,
            )
            report.save()

            serializer = ReportSerializer(report)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


class ReportList(generics.ListAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Report.objects.all()
    lookup_url_kwarg = 'id'
    serializer_class = ReportSerializer

