# Generated by Django 3.1.4 on 2020-12-06 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_door', '0008_auto_20201206_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorytype',
            name='desc',
            field=models.CharField(max_length=550, unique=True),
        ),
        migrations.AlterField(
            model_name='contractreqtype',
            name='desc',
            field=models.TextField(max_length=550),
        ),
        migrations.AlterField(
            model_name='documenttype',
            name='desc',
            field=models.TextField(max_length=550),
        ),
        migrations.AlterField(
            model_name='occupancytype',
            name='occupancy_type',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='ownershiptype',
            name='ownership_type',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='paymodetype',
            name='desc',
            field=models.TextField(max_length=550),
        ),
        migrations.AlterField(
            model_name='propertytype',
            name='property_type',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='statusreqtype',
            name='desc',
            field=models.TextField(max_length=550),
        ),
        migrations.AlterField(
            model_name='tenantreqtype',
            name='desc',
            field=models.TextField(max_length=550),
        ),
    ]
