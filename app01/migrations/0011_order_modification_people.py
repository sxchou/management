# Generated by Django 3.2.18 on 2023-04-13 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0010_auto_20230413_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='modification_people',
            field=models.CharField(default='周世旭', max_length=16, verbose_name='修改人'),
        ),
    ]
