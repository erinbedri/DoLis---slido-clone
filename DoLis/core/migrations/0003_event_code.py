# Generated by Django 4.1.4 on 2022-12-11 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_event_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='code',
            field=models.CharField(default='test', max_length=30),
            preserve_default=False,
        ),
    ]