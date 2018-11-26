from django.db import models
from client.models import Client

# Create your models here.


class Measurement(models.Model):

    profile = models.ForeignKey(Client, on_delete=models.CASCADE)
    current_weight = models.FloatField(default=0)
    goal_weight = models.FloatField(default=0)
    height = models.FloatField()
    body_fat = models.FloatField()
    plank = models.CharField(max_length=120)
    date = models.DateField(auto_now_add=True)
    goal_date = models.DateField()

    def __str__(self):
        return str(self.profile) + "'s measurements"

