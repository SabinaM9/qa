# Generated by Django 4.0.3 on 2022-04-10 15:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_date', models.DateField(auto_now=True, verbose_name='date')),
                ('squad', models.CharField(max_length=200, verbose_name='squad')),
                ('failed_tests', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000)], verbose_name='failedTests')),
                ('status', models.CharField(choices=[('on', 'passed'), ('of', 'failed')], max_length=10, verbose_name='Status')),
            ],
        ),
    ]
