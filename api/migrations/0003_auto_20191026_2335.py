# Generated by Django 2.2.6 on 2019-10-26 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20191026_2323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='pic',
        ),
        migrations.AddField(
            model_name='note',
            name='body',
            field=models.TextField(default=True),
        ),
        migrations.AddField(
            model_name='note',
            name='title',
            field=models.CharField(default=True, max_length=200),
        ),
    ]
