from .models import *
from rest_framework.serializers import ModelSerializer


class RequestPriceSerializer(ModelSerializer):
    class Meta:
        model = RequestPrice
        fields = '__all__'


class AskQuestionSerializer(ModelSerializer):
    class Meta:
        model = AskQuestion
        fields = '__all__'


class WriteDirectorSerializer(ModelSerializer):
    class Meta:
        model = WriteDirector
        fields = '__all__'


class SlideSerializer(ModelSerializer):
    class Meta:
        model = Slide
        fields = '__all__'


class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

class InfoSerializer(ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'