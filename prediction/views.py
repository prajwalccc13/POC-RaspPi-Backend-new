from prediction.utils import predict_disease
from .apps import PredictionConfig

from prediction.models import RawImage, Report, Disease, RawImageMobile, ReportMobile
from prediction.serializers import (
    RawImageSerializer, 
    ReportSerializer,
    RawImageMobileSerializer,
    ReportMobileSerializer
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



# class RawImageMobileList(APIView):
#     '''
#     Save image for prediction
#     '''
#     # permission_classes = [permissions.IsAuthenticated]    

#     def get(self, request, format=None):
#         images = RawImage.objects.all()
#         serializer = RawImageSerializer(images, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         data = request.data

#         try:
#             raw_image = RawImageMobile(
#                 image=data['image']
#             )
#             raw_image.save()

#             # img_path = raw_image.image.path

#             # result = PredictionConfig.predict_disease(img_path=img_path)
#             # result = predict_disease(img_path=img_path)
#             # # print(result)

#             # disease = Disease.objects.get(name=result)
#             # report = Report(
#             #     user= user,
#             #     raw_image= raw_image,
#             #     disease= disease,
#             # )
#             # report.save()

#             # serializer = ReportSerializer(report)
#             return Response(raw_image.data, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             print(e)
#             return Response(e, status=status.HTTP_400_BAD_REQUEST)


class RawImageListCreateView(APIView):
    # def post(self, request, format=None):
    #     serializer = RawImageMobileSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         # hardware_session_object = HardwareSession.objects.get(id=request.data['hardware_session'])
    #         # total_images_captured = hardware_session_object.total_images_captured + 1
    #         # total_diseased_images = hardware_session_object.total_diseased_images + 1
    #         # print(total_images_captured)
    #         # print('-----------------')
    #         # hardware_session = HardwareSession(
    #         #     id=request.data['hardware_session'], 
    #         #     is_image_capture=False, 
    #         #     is_current_session=True,
    #         #     total_images_captured=total_images_captured,
    #         #     total_diseased_images=total_diseased_images
    #         # )  
    #         # hardware_session.save()
    #         # return Response(serializer.data, status=status.HTTP_201_CREATED)

    #         img_path = raw_image.image.path

    #         result = PredictionConfig.predict_disease(img_path=img_path)
    #         result = predict_disease(img_path=img_path)
    #         # print(result)

    #         disease = Disease.objects.get(name=result)
    #         report = Report(
    #             user= user,
    #             raw_image= raw_image,
    #             disease= disease,
    #         )
    #         report.save()

    #         # serializer = ReportSerializer(report)
    #         return Response(raw_image.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def post(self, request, format=None):
        data = request.data

        try:
            raw_image = RawImageMobile(
                image=data['image']
            )
            raw_image.save()

            img_path = raw_image.image.path

            # print('-------------Here')

            # result = PredictionConfig.predict_disease(img_path=img_path)
            result = predict_disease(img_path=img_path)
            print(result)

            ALTERNARIA_LEAF_SPOT = 'ALF'
            BLACK_ROT = 'BR'
            CABBAGE_APHID = 'CA'
            CABBAGE_LOOPER = 'CL'
            HEALTHY_LEAF = 'HL'
            DISEASE_CHOICES = [
                (ALTERNARIA_LEAF_SPOT, 'Alternaria Leaf Spot'),
                (CABBAGE_APHID, 'Cabbage Aphid'),
                (CABBAGE_LOOPER, 'Cabbage Looper'),
                (BLACK_ROT, 'Black Rot'),
                (HEALTHY_LEAF, 'Heathy Leaf')
            ]

            print(DISEASE_CHOICES)

            disease = Disease.objects.get(name=result)
            print('-----------')
            report = ReportMobile(
                raw_image= raw_image,
                disease= disease,
            )
            report.save()

            # print('there--------------')
            # print(report)

            
            report = ReportMobile.objects.get(id=report.id)
            print('near-------------')
            print(report.id)

            test = {
                'response': report.id
            }

            # serializer = ReportMobileSerializer(report)
            return Response(test, status=status.HTTP_201_CREATED)
            # return Response({'context': result}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class RawImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RawImageMobile.objects.all()
    lookup_url_kwarg = 'id'
    serializer_class = RawImageMobileSerializer
    


class ReportList(generics.ListAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Report.objects.all()
    lookup_url_kwarg = 'id'
    serializer_class = ReportSerializer


class ReportMobileList(generics.ListAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = ReportMobile.objects.all().order_by('-datetime')
    serializer_class = ReportMobileSerializer


class ReportMobileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReportMobile.objects.all()
    lookup_url_kwarg = 'id'
    serializer_class = ReportMobileSerializer

