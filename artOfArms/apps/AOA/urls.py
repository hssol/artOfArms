from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^art_of_arms$', views.main_page),
    url(r'^art_of_arms/blogs$', views.blog_page)
]