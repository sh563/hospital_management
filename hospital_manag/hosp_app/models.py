from django.db import models

class Appointment(models.Model):
    first_name=models.CharField(  max_length=60)
    last_name=models.CharField( max_length=45)
    tell_no=models.IntegerField()
    email_id= models.CharField(max_length=50)
    address= models.CharField(max_length=50)
    postal_code= models.CharField(max_length=20)
    date= models.CharField(max_length=50)
    

    