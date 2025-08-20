from django.db import models

# Create your models here.
class DataLog(models.Model):
    number = models.CharField(max_length=30)
    step = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=100, default="")
    def __unicode__(self):
        return self.number

class WhiteList(models.Model):
    number = models.CharField(max_length=30)