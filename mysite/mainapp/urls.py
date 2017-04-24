from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.detail_category, name='detail_category')
]