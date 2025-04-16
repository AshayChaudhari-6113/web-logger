# Generated by Django 4.1.5 on 2023-06-23 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0010_alter_current_temp_date_alter_current_temp_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='current_model',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='current_model',
            name='time',
            field=models.TimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='generator_speed_model',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='generator_speed_model',
            name='time',
            field=models.TimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='power_model',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='power_model',
            name='time',
            field=models.TimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='voltage_model',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='voltage_model',
            name='time',
            field=models.TimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='windspeed_model',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='windspeed_model',
            name='time',
            field=models.TimeField(auto_now=True, null=True),
        ),
    ]
