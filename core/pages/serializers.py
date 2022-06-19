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