# Generated by Django 5.0.4 on 2024-05-11 11:50

import core.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[core.models.Validator_Email, django.core.validators.EmailValidator()]),
        ),
    ]
