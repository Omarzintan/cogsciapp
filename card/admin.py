from django.contrib import admin

# Register your models here.
from .models import Card
from .models import TrainingCard

admin.site.register(Card)
admin.site.register(TrainingCard)
