# Generated by Django 5.1.2 on 2024-10-18 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_alter_vendor_is_msmse'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='firm_type',
            field=models.CharField(choices=[('Public Ltd Co', 'Public Ltd Co'), ('Private Ltd Co', 'Private Ltd Co'), ('LLP', 'LLP'), ('Partnership firm', 'Partnership firm'), ('Proprietorship', 'Proprietorship'), ('Others', 'Others')], default='Others', max_length=50),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendor_type',
            field=models.CharField(choices=[('Public Ltd Co', 'Public Ltd Co'), ('Private Ltd Co', 'Private Ltd Co'), ('LLP', 'LLP'), ('Partnership firm', 'Partnership firm'), ('Proprietorship', 'Proprietorship'), ('Others', 'Others')], max_length=50),
        ),
    ]
