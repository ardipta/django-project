from django.db import models


# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    description = models.TextField(blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    is_mvp = models.BooleanField(default=False)
    contact_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
