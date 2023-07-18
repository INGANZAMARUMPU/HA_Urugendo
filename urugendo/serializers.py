from rest_framework import serializers
from .models import *

class IngenziSerializer(serializers.ModelSerializer):
    class Meta:
        models = Ingenzi
        fields = "__all__"
   
class UrugendoSerializer(serializers.ModelSerializer):
    class Meta:
        models = Urugendo
        fields = "__all__"
    
class ItikeSerializer(serializers.ModelSerializer):
    class Meta:
        models = Itike
        fields = "__all__"