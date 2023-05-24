# Generated by Django 4.2 on 2023-05-04 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0010_remove_emp_request_leave_leave_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp_request_leave',
            name='is_approved',
        ),
        migrations.AlterField(
            model_name='emp_request_leave',
            name='status',
            field=models.TextField(default='pending', null=True, verbose_name='Status'),
        ),
    ]
