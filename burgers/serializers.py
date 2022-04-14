from rest_framework import serializers
from .models import Burgers


class BurgerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Burgers
        fields = ['id', 'name', 'img', 'date']