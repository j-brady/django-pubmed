from django.shortcuts import render
from .models import Publication,SearchTerm

def publications_page(request):
  pubs   = Publication.objects.all()
  terms  = SearchTerm.objects.all()  
  return render(request,'publications.html',{'pubs':pubs,'search_terms':terms})

