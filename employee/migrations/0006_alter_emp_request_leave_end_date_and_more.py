# Generated by Django 4.2 on 2023-05-03 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_emp_request_leave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp_request_leave',
            name='End_Date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emp_request_leave',
            name='Start_Date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
