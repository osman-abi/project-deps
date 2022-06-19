from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView, ListAPIView
# Page Views
from .about.views import AboutAPIView, OurTeamAPIView


# Create your views here.


class AskQuestionAPIView(CreateAPIView):
    queryset = AskQuestion.objects.all()
    serializer_class = AskQuestionSerializer


class WriteDirectorAPIView(CreateAPIView):
    queryset = WriteDirector.objects.all()
    serializer_class = WriteDirectorSerializer
    permission_classes = [AllowAny]


class RequestPriceAPIView(CreateAPIView):
    queryset = RequestPrice.objects.all()
    serializer_class = RequestPriceSerializer
    permission_classes = [AllowAny]


class SlideAPIView(ListAPIView):
    queryset = Slide.objects.all()
    serializer_class = SlideSerializer
    permission_classes = [AllowAny]


ask_question_api = AskQuestionAPIView.as_view()
write_director_api = WriteDirectorAPIView.as_view()
request_price_api = RequestPriceAPIView.as_view()
about_api = AboutAPIView.as_view()
our_team_api = OurTeamAPIView.as_view()
slide_api = SlideAPIView.as_view()
