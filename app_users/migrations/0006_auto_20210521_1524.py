# Generated by Django 3.1.7 on 2021-05-21 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_user', '0005_auto_20210521_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='appusers', to=settings.AUTH_USER_MODEL),
        ),
    ]
