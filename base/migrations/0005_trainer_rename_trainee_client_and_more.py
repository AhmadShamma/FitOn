# Generated by Django 5.0.4 on 2024-05-11 13:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_trainee_gender'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=6)),
                ('bio', models.TextField(blank=True, null=True)),
                ('specialities', models.CharField(max_length=200)),
                ('experience_years', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('working_hours', models.CharField(max_length=100)),
                ('instagram_profile', models.URLField(blank=True, null=True)),
                ('twitter_profile', models.URLField(blank=True, null=True)),
                ('linkedin_profile', models.URLField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Trainer',
            },
        ),
        migrations.RenameModel(
            old_name='Trainee',
            new_name='Client',
        ),
        migrations.RemoveConstraint(
            model_name='client',
            name='Check_Gender',
        ),
        migrations.AddConstraint(
            model_name='client',
            constraint=models.CheckConstraint(check=models.Q(('gender', 'M'), ('gender', 'F'), _connector='OR'), name='Check_Trainee_Gender'),
        ),
        migrations.AddField(
            model_name='trainer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='trainer',
            constraint=models.CheckConstraint(check=models.Q(('gender', 'M'), ('gender', 'F'), _connector='OR'), name='Check_Trainer_Gender'),
        ),
    ]
