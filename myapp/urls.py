from django.urls import path
from . import views
from .sitemaps import ContactSitemap, StaticViewSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'contact': ContactSitemap,
    'static': StaticViewSitemap,
}
urlpatterns = [
    path('', views.home, name='index'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('home', views.home, name='home'),
]
