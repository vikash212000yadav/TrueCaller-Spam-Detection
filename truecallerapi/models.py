from django.db import models


# Create your models here.

class Contact(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)
    contact = models.CharField(max_length=10)
    email = models.EmailField(max_length=128)
    spam = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='contacts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
