from . models import *
from . serializers import ProfileSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class ProfileView(APIView):
    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'msg': 'Resume Upload Successfully',
                'status': 'success', 'candidate': serializer.data
            },
            status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            candidates = Profile.objects.get(id = id)
            serializer = ProfileSerializer(candidates)
            return Response({'status':'success', 'candidate':serializer.data,}, status=status.HTTP_200_OK)
        else:
            candidates = Profile.objects.all()
            serializer = ProfileSerializer(candidates,many=True)
            return Response({'status':'success', 'candidate':serializer.data,}, status=status.HTTP_200_OK)
    
    def put(self, request,pk, format=None):
        id = pk
        candidates = Profile.objects.get(id = id)
        serializer = ProfileSerializer(candidates, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request,pk, format=None):
        id = pk
        candidates = Profile.objects.get(id = id)
        serializer = ProfileSerializer(candidates, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        id = pk
        candidates = Profile.objects.get(id = id)
        candidates.delete()
        return Response({'msg':'data deleted'})