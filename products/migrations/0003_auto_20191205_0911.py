# Generated by Django 2.2 on 2019-12-05 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20191204_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='price',
            name='start_date',
            field=models.DateField(),
        ),
    ]
