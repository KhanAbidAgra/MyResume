from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    mobileNumber = models.IntegerField()
    companyName = models.CharField(max_length=100)
    cityName = models.CharField(max_length=30)
    countryName = models.CharField(max_length=30)
    msgContent = models.CharField(max_length=250)
    msgDate = models.DateField()


    def __str__(self):
        return self.name
     

