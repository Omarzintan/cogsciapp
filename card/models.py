from django.db import models

# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images/')
    answer = models.IntegerField()
    correct = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)

class TrainingCard(models.Model):
    title = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images/')
    answer = models.IntegerField()
    correct = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)


def title(self):
    return self.title
