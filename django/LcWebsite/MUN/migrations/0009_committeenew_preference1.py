# Generated by Django 2.2.2 on 2019-07-01 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MUN', '0008_remove_committeenew_preference1'),
    ]

    operations = [
        migrations.AddField(
            model_name='committeenew',
            name='preference1',
            field=models.CharField(default='None', max_length=150),
        ),
    ]