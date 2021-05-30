# Generated by Django 3.1.4 on 2021-05-30 11:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_config', '0001_initial'),
        ('new_door', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TenantContract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_no', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('discount', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('annual_rent', models.PositiveIntegerField(blank=True, null=True)),
                ('security_dep', models.PositiveIntegerField(blank=True, null=True)),
                ('commission', models.PositiveIntegerField(blank=True, null=True)),
                ('installments', models.PositiveIntegerField(blank=True, null=True)),
                ('remark', models.TextField(blank=True, max_length=550, null=True)),
                ('sms_notify', models.BooleanField(default='False')),
                ('email_notify', models.BooleanField(default='False')),
                ('contract_request', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_config.contractreqtype')),
                ('contract_status', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_config.statusreqtype')),
                ('property_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='new_door.property')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('unit', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='new_door.unit')),
            ],
        ),
    ]
