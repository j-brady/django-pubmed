from django.contrib import admin
from .models import Publication,SearchTerm#,Email 
from .pubmed import GetPubMedEntries,convert_to_string

def get_pubmed_entry(modeladmin,request,queryset):
  for p in queryset:
    email = p.email
    search_term=p.search_term    
    records = GetPubMedEntries(email,search_term)

    for record in records:
      author_list  = convert_to_string(record,"AU")
      title_temp   = convert_to_string(record,"TI")
      journal_temp = convert_to_string(record,"SO")
      year_temp    =  ''
      pmid_temp    = convert_to_string(record,"PMID")
      a = Publication(authors=author_list,year=year_temp,title=title_temp,journal=journal_temp,volume_issue_pages='',search_term=search_term,pmid=pmid_temp)
      # Save changes to the database if entry is unique - This is very inefficient though
      check_unique(new_publication=a)

def delete_publications_from_list(modeladmin,request,queryset):
  for p in queryset:
    search_term = p.search_term
    Publication.objects.filter(search_term=search_term).delete()
    
      
def check_unique(new_publication):
  # Function to check that entries are unique
  # filters against (title, search_term) tuple.
  pubs   = Publication.objects.all()
  titles = [(pub.title,pub.search_term) for pub in pubs]
  if (new_publication.title,new_publication.search_term) in titles:
    pass
  else:
    new_publication.save()
    


# This is the name of the function in the admin drop down menu
get_pubmed_entry.short_description = "Fetch Pubmed entry"

class PublicationAdmin(admin.ModelAdmin):
  list_display = ('authors', 'year','search_term')

class SearchTermAdmin(admin.ModelAdmin):
  list_display = ('search_name','search_term')
  actions = [get_pubmed_entry,delete_publications_from_list] 

admin.site.register(Publication,PublicationAdmin)
admin.site.register(SearchTerm,SearchTermAdmin)
