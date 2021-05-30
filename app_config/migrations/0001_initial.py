# Generated by Django 3.1.4 on 2021-05-30 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_type', models.CharField(max_length=50, unique=True)),
                ('desc', models.CharField(blank=True, max_length=550, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docs_type', models.CharField(max_length=50)),
                ('num_of_doc', models.IntegerField(default=2)),
                ('desc', models.TextField(blank=True, max_length=550, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OccupancyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupancy_type', models.CharField(max_length=50, unique=True)),
                ('desc', models.TextField(blank=True, max_length=550, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OwnershipType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ownership_type', models.CharField(max_length=50, unique=True)),
                ('desc', models.TextField(blank=True, max_length=550, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PayModeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_type', models.CharField(max_length=50)),
                ('desc', models.TextField(blank=True, max_length=550, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StatusReqType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('str_req', models.CharField(max_length=50)),
                ('desc', models.TextField(blank=True, max_length=550, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TenantReqType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_req_type', models.CharField(max_length=50)),
                ('desc', models.TextField(blank=True, max_length=550, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_type', models.CharField(max_length=100, unique=True)),
                ('desc', models.TextField(blank=True, max_length=550, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_config.categorytype')),
            ],
        ),
        migrations.CreateModel(
            name='ContractReqType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_req', models.CharField(max_length=50)),
                ('desc', models.TextField(blank=True, max_length=550, null=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]