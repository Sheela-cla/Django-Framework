# Generated by Django 5.0.4 on 2024-05-08 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Last_name',
            new_name='last_name',
        ),
    ]
