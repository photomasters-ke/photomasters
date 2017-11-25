from django.conf.urls import url
from django.core.urlresolvers import reverse
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name="home"),
    url(r'^categories', views.categories_page, name="categories"),
    url(r'^pricing$', views.pricing, name="pricing"),
    url(r'^maestro', views.maestro, name="maestro"),
    url(r'^about', views.about_us, name="about"),
    url(r'^contact/', views.contact, name="contact")
]
