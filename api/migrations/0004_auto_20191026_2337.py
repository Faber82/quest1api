# Generated by Django 2.2.6 on 2019-10-26 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20191026_2335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='body',
            new_name='pic',
        ),
        migrations.RemoveField(
            model_name='note',
            name='title',
        ),
    ]
