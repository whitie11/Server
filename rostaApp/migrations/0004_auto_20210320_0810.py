# Generated by Django 3.1.5 on 2021-03-20 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rostaApp', '0003_auto_20210320_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='selected_duties',
            field=models.JSONField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='config',
            name='selected_staff',
            field=models.JSONField(default=''),
            preserve_default=False,
        ),
    ]
