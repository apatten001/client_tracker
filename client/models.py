from django.db import models

# Create your models here.


class Client(models.Model):

    first_name = models.CharField(max_length=120, blank=False)
    last_name = models.CharField(max_length=120, blank=False)
    Birthday = models.DateField()
    phone_number = models.CharField(max_length=30, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


