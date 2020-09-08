from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("khanh", views.khanh, name="khanh"),
    path("<str:name>", views.greet, name="greet")
]