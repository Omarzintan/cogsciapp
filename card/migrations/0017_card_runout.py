# Generated by Django 2.0.2 on 2019-04-24 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0016_answercard'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='runout',
            field=models.IntegerField(default=0),
        ),
    ]
