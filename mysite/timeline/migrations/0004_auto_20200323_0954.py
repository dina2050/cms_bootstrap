# Generated by Django 2.2.11 on 2020-03-23 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0003_auto_20200323_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
