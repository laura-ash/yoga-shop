from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.blog_home),
    url(r'^(?P<slug>[\w-]+)/$', views.blog_post, name="detail"),
]