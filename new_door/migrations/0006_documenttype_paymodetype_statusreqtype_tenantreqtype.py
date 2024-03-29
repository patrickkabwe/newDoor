# Generated by Django 3.1.4 on 2020-12-05 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_door', '0005_contractreqtype_tenantcontract'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docs_type', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=550)),
            ],
        ),
        migrations.CreateModel(
            name='PayModeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_type', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=550)),
            ],
        ),
        migrations.CreateModel(
            name='StatusReqType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('str_qty', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=550)),
            ],
        ),
        migrations.CreateModel(
            name='TenantReqType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_req_type', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=550)),
            ],
        ),
    ]
