# Generated by Django 4.2.1 on 2024-02-19 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_payable_feel_students_payable_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='time_slot',
            field=models.CharField(choices=[('10:00 a.m', '12:00 p.m'), ('1:00 a.m', '3:00 p.m'), ('3:00 a.m', '5:00 p.m')], max_length=200),
        ),
    ]
