from django.contrib import admin

# Register your models here.
from .models import Card
from .models import TrainingCard
from .models import AnswerCard
from .models import ExampleCard

admin.site.register(Card)
admin.site.register(TrainingCard)
admin.site.register(AnswerCard)
admin.site.register(ExampleCard)
