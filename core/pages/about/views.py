from .serializers import *
from .models import *
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny


class AboutAPIView(ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [AllowAny]


class OurTeamAPIView(ListAPIView):
    queryset = OurTeam.objects.all()
    serializer_class = OurTeamSerializer
    permission_classes = [AllowAny]
