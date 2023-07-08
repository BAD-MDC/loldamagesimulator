# backend/post/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import StatList,StatDetail
# ,stat_save
urlpatterns = [
    path('stats/',StatList.as_view()),
    path('stats/<str:pk>/',StatDetail.as_view()),
    # path('stats_save/',stat_save()),
]

urlpatterns=format_suffix_patterns(urlpatterns)