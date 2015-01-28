from django.db import models
 

class Publication(models.Model):
  
  authors = models.CharField(max_length=1000,blank=True,null=True)
  year    = models.CharField(max_length=4,blank=True,null=True)
  title   = models.CharField(max_length=500,blank=True,null=True)
  journal = models.CharField(max_length=500,blank=True,null=True)
  volume_issue_pages = models.CharField(max_length=100,blank=True,null=True)
  
  email       =  models.EmailField(blank=True,null=True)
  search_term =  models.CharField(max_length=500,blank=True,null=True)

  def __str__(self):
    return '%s'%self.authors
