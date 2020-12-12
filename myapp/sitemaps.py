from django.contrib.sitemaps import Sitemap
from .models import Contact
from django.urls import reverse
class ContactSitemap(Sitemap):
    def items(self):
        return Contact.objects.all()



class StaticViewSitemap(Sitemap):
    def items(self):
        return['index']
    def location(self,item):
        return reverse(item)