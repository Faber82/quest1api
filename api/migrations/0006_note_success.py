# Generated by Django 2.2.6 on 2019-10-27 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20191027_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='success',
            field=models.BooleanField(default=True),
        ),
    ]
