# Generated by Django 3.1.4 on 2021-02-13 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new_door', '0007_remove_payment_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='new_door.unit'),
        ),
    ]
