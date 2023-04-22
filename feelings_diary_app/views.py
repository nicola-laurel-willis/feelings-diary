from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import dateformat, timezone
from django.urls import reverse

from .models import DiaryEntry

# Create your views here.

def index(request):
  diary_entry_list = DiaryEntry.objects.order_by("-pub_date")
  context = {"diary_entry_list": diary_entry_list}
  return render(request, "feelings_diary_app/index.html", context)
  
def save_entry(request):
  text_input = request.POST["text-input"]
  publication_date=timezone.now()
  entry = DiaryEntry(entry_text=text_input, pub_date=timezone.now())
  entry.save()
  
  return HttpResponseRedirect(reverse("feelings_diary_app:index"))
  