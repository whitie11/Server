# Generated by Django 3.1.5 on 2021-03-22 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_staff_initials'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alloc',
            name='isAM',
        ),
        migrations.AlterField(
            model_name='staff',
            name='userName',
            field=models.CharField(max_length=26, unique=True),
        ),
    ]
