# Generated by Django 3.1.5 on 2021-02-28 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210206_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='initials',
            field=models.CharField(default='AA', max_length=3),
            preserve_default=False,
        ),
    ]