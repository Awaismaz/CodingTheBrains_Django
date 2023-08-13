from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
fs = FileSystemStorage(location=settings.MEDIA_ROOT)

# Create your models here.

class Profile(models.Model):
    GENDER_COICES=[
        ('M','Male'),
        ('F','Female'),
    ]
    name=models.CharField(max_length=100)
    profile_pic=models.ImageField(null=True, blank=True)
    age=models.IntegerField()
    gender=models.CharField(max_length=1, choices=GENDER_COICES)
    occupation=models.CharField(max_length=100,null=True, blank=True)
    birth_date=models.DateField(null=True)
    is_married=models.BooleanField(default=False)
    email=models.EmailField(max_length=254, unique=True)

    def save(self, *args, **kwargs):
        print(f"Data Updated for {self.name}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


    