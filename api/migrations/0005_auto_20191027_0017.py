# Generated by Django 2.2.6 on 2019-10-26 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20191026_2337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='pic',
            new_name='img_url',
        ),
    ]
