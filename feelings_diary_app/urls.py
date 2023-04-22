from django.urls import path
from . import views

app_name = "feelings_diary_app"
urlpatterns = [
  path("", views.index, name="index"),
  path("save-entry/", views.save_entry, name="save_entry"),
]