# Generated by Django 2.0.2 on 2019-04-25 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0017_card_runout'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
