from rest_framework import serializers
from .models import Worker, Unit , Visit



class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['pk' , 'name']

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ['pk' , 'date_time']