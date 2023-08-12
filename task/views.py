from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import viewsets , generics 
from rest_framework.filters import SearchFilter 
from .models import Worker , Unit , Visit
from .serializers import WorkerSerializer , UnitSerializer , VisitSerializer
from rest_framework.permissions import IsAdminUser


@api_view(['GET'])
def units_list(request):
    worker = Worker.objects.get(phone_number = request.data['phone_number'])
    units = Unit.objects.filter(worker=worker)
    serializer = UnitSerializer(units , many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def make_a_visit(request):
    worker = Worker.objects.get(phone_number = request.data['phone_number'])
    unit = Unit.objects.get(pk = request.data['unit_pk'])
    if worker == unit.worker:
        serializer = VisitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else :
        response = {
        'Error': 'you are not authenticated to make this visit'
    }
        return JsonResponse (response)
    


class WorkerAPI(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']
    permission_classes = [IsAdminUser]


class UnitAPI(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']
    permission_classes = [IsAdminUser]


class VisitAPI(generics.ListAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    filter_backends = [SearchFilter]
    search_fields = ['unit']
    permission_classes = [IsAdminUser]

    def find_worker(request):
        worker = Worker.objects.filter(name = request.data['name'])
        serializer = WorkerSerializer(worker , many=True)
        return Response(serializer.data)
    
    def find_unit(request):
        unit = Unit.objects.filter(name = request.data['name'])
        serializer = UnitSerializer(unit , many=True)
        return Response(serializer.data)
    




