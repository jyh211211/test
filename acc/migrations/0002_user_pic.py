# Generated by Django 4.0.6 on 2022-09-01 01:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pic',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='user/%y/%m'),
            preserve_default=False,
        ),
    ]
