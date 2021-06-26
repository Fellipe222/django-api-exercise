from django.db import models

class Customer(models.Model):
    GENDER = (
        ('Undefined', 'U'),
        ('Male', 'M'),
        ('Female', 'F')
    )
    req_status  = models.CharField(max_length=50)
    first_name  = models.CharField(max_length=200)
    last_name   = models.CharField(max_length=200)
    email       = models.CharField(max_length=100)
    gender      = models.CharField(max_length=10, choices=GENDER, default='U')
    company     = models.CharField(max_length=100)
    city        = models.CharField(max_length=50)
    title       = models.CharField(max_length=50)
    lat         = models.CharField(max_length=100)
    lgn         = models.CharField(max_length=100)

    def __str__(self):
        return self.id
