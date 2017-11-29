from django.conf.urls import url
from profiles import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
  

]
