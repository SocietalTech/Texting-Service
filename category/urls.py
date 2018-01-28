from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'attribute_create$', views.attribute_create, name='attribute_create'),
    url(r'category_create$', views.category_create, name='category_create'),
    url(r'sms$', views.sms, name='sms'),
]
