# Generated by Django 3.2.7 on 2021-10-22 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20211022_0356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='dev_data',
            new_name='Development_data',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='mon_data',
            new_name='Monitoring_data',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='obj_file',
            new_name='Object_file',
        ),
    ]
