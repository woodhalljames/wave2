# Generated by Django 3.1.7 on 2021-05-21 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0003_auto_20210521_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='user_type',
            field=models.CharField(choices=[('Cust', 'Customer'), ('sel', 'Seller')], default='cust', max_length=100),
        ),
    ]
