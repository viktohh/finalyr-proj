# Generated by Django 3.2.5 on 2021-07-21 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_logged_in',
            field=models.BooleanField(default=False),
        ),
    ]
