from rest_framework import serializers
from .models import MoneyImageModel


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoneyImageModel
        fields = '__all__'

