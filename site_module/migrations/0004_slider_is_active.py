# Generated by Django 5.0 on 2023-12-20 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0003_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال / غیرفعال'),
        ),
    ]