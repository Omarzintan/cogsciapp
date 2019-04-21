from django.db import models

class Result(models.Model):
    cardtitle = models.IntegerField()
    correct = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)
