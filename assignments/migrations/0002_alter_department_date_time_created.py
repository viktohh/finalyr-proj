# Generated by Django 3.2.5 on 2021-07-21 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='date_time_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
