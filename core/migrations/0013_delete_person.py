# Generated by Django 5.0.4 on 2024-05-11 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_delete_trainer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]