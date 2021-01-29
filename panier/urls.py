from django.urls import path
from .views import ChariotList

urlpatterns=[
    # url du chariot
    path('',ChariotList.as_view()),

]