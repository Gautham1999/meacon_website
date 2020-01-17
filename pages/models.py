from django.db import models

# Create your models here.
class Participant(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    college = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    mobile = models.CharField(max_length=13)
    year = models.CharField(max_length=10)
    non_veg = models.NullBooleanField(null=True)
    def __str__(self):
        return self.name
