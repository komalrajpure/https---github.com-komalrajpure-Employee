# Generated by Django 4.2 on 2023-05-08 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0013_alter_emp_request_leave_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp_request_leave',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]