# Generated by Django 4.0.3 on 2022-04-09 18:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0002_alter_testresults_failed_tests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresults',
            name='failed_tests',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='failedTests'),
        ),
    ]
