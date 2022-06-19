from .models import *
from rest_framework.serializers import ModelSerializer


class AboutSerializer(ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class OurTeamSerializer(ModelSerializer):
    class Meta:
        model = OurTeam
        fields = '__all__'
