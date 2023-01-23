from rest_framework import serializers
from .models import Province

class Province_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Province
        fields = ['id', 'province_name']