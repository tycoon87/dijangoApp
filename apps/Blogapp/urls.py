from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.index),
url(r'^new$', views.new),
url(r'^show/(?P<Blog_id>\d+)$' , views.show),
url(r'^(?P<Blog_id>\d+)/editblog$' , views.editblog),
url(r'^(?P<Blog_id>\d+)/delete$' , views.delete)
]
