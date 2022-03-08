from rest_framework import serializers
from .models import *


class TimeSlotSerializer(serializers.ModelSerializer):

    available_time_slot = serializers.SerializerMethodField()

    def get_available_time_slot(self, obj):
        response_data = StadiumAvailabililty.objects.filter(id=obj.id)
        return SlotsSerializer(response_data, many=True).data

    stadium_info = serializers.SerializerMethodField()

    def get_stadium_info(self, obj):
        response_data = Stadium.objects.filter(id=obj.stadium_id_id )
        return StadiumSerializer(response_data, many=True).data

    class Meta:
        model = StadiumAvailabililty
        fields = ('available_time_slot', 'stadium_info')


class SlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StadiumAvailabililty
        fields = '__all__'


class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = '__all__'