# Generated by Django 4.1.5 on 2023-07-31 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0025_time_stamp_date_rig_time_stamp_time_rig'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='voltage_model',
            new_name='voltageR_model',
        ),
        migrations.RenameModel(
            old_name='voltage_parameters',
            new_name='voltageR_parameters',
        ),
        migrations.RenameModel(
            old_name='voltage_temp',
            new_name='voltageR_temp',
        ),
    ]
