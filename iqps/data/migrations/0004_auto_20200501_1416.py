# Generated by Django 3.0.4 on 2020-05-01 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20200501_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='code',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
