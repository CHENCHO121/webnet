from django.db import models
from django.urls import reverse
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=15)
    message=models.TextField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Contact'

    def get_absolute_url(self):
        return reverse('home')