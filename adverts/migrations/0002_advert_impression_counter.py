# Generated by Django 2.2.6 on 2019-11-13 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='impression_counter',
            field=models.IntegerField(default=0),
        ),
    ]