from turtle import update
from django.db import models

# Create your models here.

class Student(models.Model):

    YEAR_IN_SCHOOL_CHOICES = [
        ("FR", 'Freshman'),
        ("SP", 'Sophomore'),
        ("JR", 'Junior'),
        ("SR", 'Senior'),
        ("GRD", 'Graduate'),
    ]

    first_name= models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number= models.IntegerField()
    about = models.TextField(null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to= 'media/p')
    register_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    year_in_school = models.CharField(max_length=3, choices=YEAR_IN_SCHOOL_CHOICES, default="FR")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
          # veya return self.first_name  #admin panelde tablo başlıklarının hangi isimle görüneceği

    class Meta:

        ordering = ["number"]
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        # admin paneldeki görünürlükler
