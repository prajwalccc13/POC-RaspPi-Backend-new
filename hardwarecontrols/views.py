from logging import exception
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 

from .models import (
    HardwareInfo,
    HardwareSession,
    SessionImage
)
from .serializers import (
    HardwareInfoSerializer,
    HardwareSessionSerializer,
    SessionImageSerializer
)


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening

# HardwareInfo Views

class HardwareInfoListCreateView(generics.ListCreateAPIView):
    queryset = HardwareInfo.objects.all()
    serializer_class = HardwareInfoSerializer

# class HardwareInfoDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = HardwareInfo.objects.all()
#     lookup_url_kwarg = 'id'
#     serializer_class = HardwareInfoSerializer


class HardwareInfoDetailView(APIView):
    def get_object(self, pk):
        try:
            return HardwareInfo.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, id, format=None):
        try:
            hardware_id = self.get_object(id)
            serializer = HardwareInfoSerializer(hardware_id)
            return Response(serializer.data)
        except Exception:
            return Response("No Active sessions.", status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, id, format=None):
        hardware_id = self.get_object(id)
        serializer = HardwareInfoSerializer(hardware_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            if(request.data['is_process_started']):
                hardware_session = HardwareSession(hardware_info=hardware_id, is_current_session=True)  
                hardware_session.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# HardwareSession Views

class HardwareSessionListCreateView(generics.ListCreateAPIView):
    queryset = HardwareSession.objects.all().order_by('-datetime').values()
    serializer_class = HardwareSessionSerializer

class HardwareSessionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HardwareSession.objects.all()
    lookup_url_kwarg = 'id'
    serializer_class = HardwareSessionSerializer

# class HardwareSessionDetailView(APIView):
#     def get_object(self, id):
#         try:
#             return HardwareSession.objects.get(pk=id)
#         except:
#             raise Http404

#     def get(self, request, id, format=None):
#         try:
#             hardware_id = self.get_object(id)
#             serializer = HardwareSessionSerializer(hardware_id)
#             return Response(serializer.data)
#         except Exception:
#             return Response("No Active sessions.", status=status.HTTP_204_NO_CONTENT)

#     def patch(self, request, id, format=None):
#         hardware_id = self.get_object(id)
#         serializer = HardwareSessionSerializer(hardware_id, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CurrentHardwareSession(APIView):
    '''
    Get current active session
    '''

    def get(self, request, format=None):
        try:
            session = HardwareSession.objects.get(is_current_session = True)
            serializer = HardwareSessionSerializer(session, many=False)
            return Response(serializer.data)
        except Exception:
            return Response("No Active sessions.", status=status.HTTP_204_NO_CONTENT)

class SetCurrentHardwareSessionImageCapture(APIView):
    def get(self, request, format=None):
        try:
            session = HardwareSession.objects.get(is_current_session = True)
            print(session['is_image_capture'])
            serializer = HardwareSessionSerializer(session, many=False)
            return Response(serializer.data)
        except Exception:
            return Response("No Active sessions.", status=status.HTTP_204_NO_CONTENT)



# SessionImage View

# class SessionImageListCreateView(generics.ListCreateAPIView):
#     queryset = SessionImage.objects.all()
#     serializer_class = SessionImageSerializer

class SessionImageListCreateView(APIView):
    def post(self, request, format=None):
        serializer = SessionImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            hardware_session_object = HardwareSession.objects.get(id=request.data['hardware_session'])
            total_images_captured = hardware_session_object.total_images_captured + 1
            total_diseased_images = hardware_session_object.total_diseased_images + 1
            # print(total_images_captured)
            # print('-----------------')
            hardware_session = HardwareSession(
                id=request.data['hardware_session'], 
                is_image_capture=False, 
                is_current_session=True,
                total_images_captured=total_images_captured,
                total_diseased_images=total_diseased_images
            )  
            hardware_session.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SessionImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SessionImage.objects.all()
    lookup_url_kwarg = 'id'
    serializer_class = SessionImageSerializer
    