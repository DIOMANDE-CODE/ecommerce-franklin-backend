from django.urls import path
from .views import ClientList

urlpatterns=[
    # url du chariot
    path('',ClientList.as_view()),

]