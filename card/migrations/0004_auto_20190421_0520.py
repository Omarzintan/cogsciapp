# Generated by Django 2.0.2 on 2019-04-21 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0003_auto_20190421_0517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='answer',
            field=models.IntegerField(),
        ),
    ]
