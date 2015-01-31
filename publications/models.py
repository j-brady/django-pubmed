from django.db import models
 

class Publication(models.Model):
  
  authors = models.CharField(max_length=1000,blank=True)
  year    = models.CharField(max_length=4,blank=True)
  title   = models.CharField(max_length=500,blank=True)
  journal = models.CharField(max_length=500,blank=True)
  volume_issue_pages = models.CharField(max_length=100,blank=True)
  
  search_term =  models.CharField(blank=True,max_length=500)

  def __str__(self):
    return '%s'%self.authors


class SearchTerm(models.Model):
  #In order to use this service you must enter your email address
  email       =  models.EmailField(blank=True)
  #Pubmed search term
  search_term =  models.CharField(max_length=500,blank=True)
  #This is the name of the search that will be rendered in HTML
  search_name =  models.CharField(max_length=500,blank=True)
  
  def __str__(self):
    return "Search term '%s' for %s"%(self.search_term,self.search_name)

#class Email(models.Model):
#  #In order to use this service you must enter your email address
#  email       =  models.EmailField(blank=True)
  
