from django.contrib import admin
from .models import Publication 
from .pubmed import GetPubMedEntries,convert_to_string

def get_pubmed_entry(modeladmin,request,queryset):
  for p in queryset:
    email = p.email
    search_term=p.search_term    
    records = GetPubMedEntries(email,search_term)
    for record in records:
      author_list = convert_to_string(record,"AU")
      title_temp = convert_to_string(record,"TI")
      journal_temp = convert_to_string(record,"SO")
      year_temp  =  ''
      a = Publication(authors=author_list,year=year_temp,title=title_temp,journal=journal_temp,volume_issue_pages='')
      a.save()
get_pubmed_entry.short_description = "Fetch Pubmed entry"

class PublicationAdmin(admin.ModelAdmin):
  list_display = ('authors', 'year','search_term')

  actions = [get_pubmed_entry] 

admin.site.register(Publication,PublicationAdmin)
