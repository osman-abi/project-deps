from django.urls import path
from .views import ask_question_api, write_director_api, about_api, our_team_api, slide_api, request_price_api

urlpatterns = [
    path('write-director/', write_director_api),
    path('ask-question/', ask_question_api),
    path('about/', about_api),
    path('our-team/', our_team_api),
    path('request-price', request_price_api),
    path('slide/', slide_api),
]