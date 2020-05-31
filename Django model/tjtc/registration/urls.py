from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register$',views.show_page),
    url(r'^save/$', views.save_data),
]