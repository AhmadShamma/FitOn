# Generated by Django 5.0.4 on 2024-05-12 05:00

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_client_trainer_client_check_client_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[core.models.validate_height]),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[core.models.phone_number_validator]),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='experience_years',
            field=models.IntegerField(default=0),
        ),
    ]
