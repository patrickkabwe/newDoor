# Generated by Django 3.1.3 on 2020-11-26 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_door', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unit',
            old_name='owner_type',
            new_name='ownership_type',
        ),
    ]
