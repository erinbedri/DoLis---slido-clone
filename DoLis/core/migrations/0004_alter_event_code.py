# Generated by Django 4.1.4 on 2022-12-11 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_event_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='code',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
