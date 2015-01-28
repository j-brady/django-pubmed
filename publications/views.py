from django.shortcuts import render
from .models import Publication

def publications_page(request):
  pubs = Publication.objects.all()
  return render(request,'publications.html',{'pubs':pubs})
