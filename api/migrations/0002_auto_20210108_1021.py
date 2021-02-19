# Generated by Django 3.1.5 on 2021-01-08 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alloc',
            name='isAM',
        ),
        migrations.AddField(
            model_name='alloc',
            name='session',
            field=models.CharField(choices=[('AM', 'morning'), ('PM', 'afternoon')], default='morning', max_length=2),
        ),
    ]
