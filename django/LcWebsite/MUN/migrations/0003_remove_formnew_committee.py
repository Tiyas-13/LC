# Generated by Django 2.2.2 on 2019-06-24 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MUN', '0002_auto_20190624_0657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formnew',
            name='Committee',
        ),
    ]
