# Generated by Django 4.2 on 2023-05-05 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0011_remove_emp_request_leave_is_approved_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp_request_leave',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
