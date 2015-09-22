from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^new/$', views.create, name='new'),
    url(r'^store/', views.store, name='store'),
    url(r'^$', views.index, name='index'),
]
