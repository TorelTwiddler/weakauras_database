from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views


urlpatterns = [
    # example: /wadb/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # example: /wadb/3/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]

urlpatterns += staticfiles_urlpatterns()