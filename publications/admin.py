from django.contrib import admin
from .models import Publication,SearchTerm#,Email 
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
      a = Publication(authors=author_list,year=year_temp,title=title_temp,journal=journal_temp,volume_issue_pages='',search_term=search_term)
      # Save changes to the database
      a.save()

# This is the name of the function in the admin drop down menu
get_pubmed_entry.short_description = "Fetch Pubmed entry"

class PublicationAdmin(admin.ModelAdmin):
  list_display = ('authors', 'year')

class SearchTermAdmin(admin.ModelAdmin):
  list_display = ('search_name','search_term')
  actions = [get_pubmed_entry] 

admin.site.register(Publication,PublicationAdmin)
admin.site.register(SearchTerm,SearchTermAdmin)
