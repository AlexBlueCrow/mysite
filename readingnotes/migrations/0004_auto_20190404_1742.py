# Generated by Django 2.1.5 on 2019-04-04 09:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('readingnotes', '0003_auto_20190324_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
