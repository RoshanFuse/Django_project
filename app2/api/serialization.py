from rest_framework import serializers
from app2.models import Data


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['id','name','image']
    









