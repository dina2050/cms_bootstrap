# Generated by Django 2.2.11 on 2020-03-23 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0005_timelinepluginmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='timelinepluginmodel',
            name='events',
            field=models.ManyToManyField(to='timeline.Event'),
        ),
    ]