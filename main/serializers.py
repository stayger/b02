from rest_framework import serializers
from .models import Conc

class ConcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conc
        fields = '__all__'