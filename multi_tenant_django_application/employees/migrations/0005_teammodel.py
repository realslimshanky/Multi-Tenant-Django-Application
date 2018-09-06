# Generated by Django 2.1 on 2018-09-05 20:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0003_auto_20180905_1644'),
        ('employees', '0004_auto_20180905_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20, verbose_name='Team Name')),
                ('description', models.TextField(verbose_name='Team description')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenants.CompanyModel')),
                ('employees', models.ManyToManyField(to='employees.EmployeeModel', verbose_name='Employees')),
            ],
            options={
                'verbose_name': 'Team',
                'ordering': ('name',),
                'verbose_name_plural': 'Teams',
            },
        ),
    ]