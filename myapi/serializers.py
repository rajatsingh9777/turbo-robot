from rest_framework import serializers

from .models import Hero

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'starting_date', 'ending_date')

"""
            
class AvailableDate(serializers.Serializer):
    name = serializers.CharField() 
    starting_date = serializers.CharField() 
    ending_date = serializers.CharField() 
"""
