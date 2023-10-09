from django.db import models

# Create your models here.
class Ritesh(models.Model):
    fname= models.CharField(max_length=25, blank=False, null=False)
    lname= models.CharField(max_length=25, blank=False, null=False)
    email= models.EmailField()
    phone= models.IntegerField()
    unit= models.IntegerField()
    bill= models.IntegerField()

    def __str__(self) :
        return self.fname
