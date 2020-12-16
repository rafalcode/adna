from django.urls import path
from dategive import views

urlpatterns = [
    path("date/", views.dgive_show, name="dgive_show"),
]
