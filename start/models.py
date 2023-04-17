from django.db import models
from ckeditor.fields import RichTextField

class Cyber(models.Model):
    name = models.CharField(max_length=255,verbose_name="ism")
    email = models.EmailField(max_length=255)
    phone = models.BigIntegerField( verbose_name='Telefon raqam')
    photo = models.ImageField(upload_to='start/images/')
    short_discription = models.TextField()
    discription = RichTextField(null=True, blank=True)
