# Generated by Django 3.1.4 on 2021-01-20 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new_door', '0049_auto_20210120_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='contract',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='new_door.tenantcontract'),
        ),
    ]
