import imp
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


@api_view(['GET'])
def home(request):
    students_objs = student.objects.all()

    serializer = studentSerializer(students_objs, many=True)
    return Response({'status':200,'payload':serializer.data})

@api_view(['POST'])
def post(request):
    data = request.data
    serializer = studentSerializer(data = request.data)

    if not serializer.is_valid():
        return Response({'status':403,'message':'something went wrong'})

    serializer.save()
    
    return Response({'status':200,'payload':serializer.data,'message':'data saved successfully'})

