from rest_framework import serializers
from .models import Magar

class MagarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magar
        fields = '__all__'