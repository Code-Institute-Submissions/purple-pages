# Generated by Django 2.2.6 on 2019-12-03 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0002_advert_impression_counter'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('template_file', models.FilePathField(match='ad_template_*', path='C:\\Users\\Kingo\\Documents\\Coding 2019\\Purple-Pages\\adverts/templates')),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]