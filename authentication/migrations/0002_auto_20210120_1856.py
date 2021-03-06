# Generated by Django 3.1.1 on 2021-01-20 16:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator(code='invalid_firstname', message='Username must be Alphanumeric', regex='^[a-zA-Z]*$')]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator(message='Username must be Alphanumeric', regex='^[a-zA-Z]*$')]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='middle_name',
            field=models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator(code='invalid_middle_name', message='Username must be Alphanumeric', regex='^[a-zA-Z]*$')]),
        ),
    ]
