from django.urls import path
from release_info import views

urlpatterns = [
    path("", views.ReleaseView.as_view(), name="release"),
]
