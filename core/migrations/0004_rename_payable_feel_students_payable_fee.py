# Generated by Django 4.2.1 on 2024-02-19 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_time_slog_students_time_slot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='payable_feel',
            new_name='payable_fee',
        ),
    ]
