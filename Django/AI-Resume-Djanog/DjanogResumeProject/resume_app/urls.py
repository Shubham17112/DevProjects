from . import views
from django.urls import path

app_name = "resume_app"

urlpatterns = [
    path("", views.index, name="index")
]
