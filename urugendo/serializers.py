from rest_framework import serializers
from .models import *

class IngenziSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingenzi
        fields = "__all__"
   
class UrugendoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urugendo
        fields = "__all__"
    
class ItikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itike
        fields = "__all__"