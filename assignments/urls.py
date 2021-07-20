from django.urls import path
from . import views

app_name = "assignments"

urlpatterns = [
    path("", views.index, name="index"),
]