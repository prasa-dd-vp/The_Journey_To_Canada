# Generated by Django 2.1.7 on 2020-05-31 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nationality',
        ),
    ]
