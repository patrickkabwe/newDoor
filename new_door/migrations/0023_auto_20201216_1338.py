# Generated by Django 3.1.4 on 2020-12-16 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_door', '0022_auto_20201214_2249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic'),
        ),
    ]
