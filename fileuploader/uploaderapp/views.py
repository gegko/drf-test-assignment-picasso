from django.http import HttpRequest
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from uploaderapp.tasks import process_file
from uploaderapp.models import File
from uploaderapp.serializers import FileSerializer


# class FileList(generics.ListCreateAPIView):
#     queryset = File.objects.all()
#     serializer_class = FileSerializer

@api_view(['GET'])
def file_list(request: HttpRequest) -> Response:
    files = File.objects.all()
    serializer = FileSerializer(files, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['POST'])
def upload(request: HttpRequest) -> Response:
    serializer = FileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        process_file.delay(serializer.data['id'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
