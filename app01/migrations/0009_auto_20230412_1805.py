# Generated by Django 3.2.18 on 2023-04-12 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_auto_20230412_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='价格'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='account',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='账户余额'),
        ),
    ]
