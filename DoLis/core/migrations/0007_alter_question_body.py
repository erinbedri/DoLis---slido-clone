# Generated by Django 4.1.4 on 2022-12-11 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_question_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='body',
            field=models.TextField(max_length=500),
        ),
    ]