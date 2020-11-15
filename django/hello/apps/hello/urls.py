from django.conf.urls import url
from hello.apps.hello import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
