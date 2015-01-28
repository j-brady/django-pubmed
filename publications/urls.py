from django.conf.urls import url,patterns
from publications import views

urlpatterns = patterns('',
       url(r'^$',views.publications_page,name="publications"),
)
