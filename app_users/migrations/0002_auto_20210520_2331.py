# Generated by Django 3.1.7 on 2021-05-20 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='appuser',
            name='city',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='appuser',
            name='gender',
            field=models.CharField(choices=[(1, 'MALE'), (2, 'FEMALE'), (3, 'OTHER')], default=1, max_length=50),
        ),
        migrations.AddField(
            model_name='appuser',
            name='mobile',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appuser',
            name='pincode',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
