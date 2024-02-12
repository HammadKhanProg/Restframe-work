from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def apioverview (request):
    api_urls={
        'home':'/home/',
        'update':'/update/<str:pk>/',
        'delete':'/delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(["GET"])
def tasklist (request):
    task=Task.objects.all()
    serializer=TaskSerializer(task,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskdetails (request,pk):
    task=Task.objects.get(id=pk)
    serializer=TaskSerializer(task, many=False)
    return Response (serializer.data)


@api_view(["POST"])
def taskcreate (request):
    serialzers=TaskSerializer(data=request.data)
    if serialzers.is_valid():
        serialzers.save()
        return Response(serialzers.data)
    
@api_view(["POST"])
def taskupdate (request,pk):
    task=Task.objects.get(id=pk)
    serializers=TaskSerializer(instance=task,data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response (serializers.data)
    
@api_view(["DELETE"])
def taskdelete (request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return Response("Item Deleted Succussfully")
    