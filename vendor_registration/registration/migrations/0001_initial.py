# Generated by Django 5.0.7 on 2024-10-10 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=255)),
                ('vendor_type', models.CharField(choices=[('Public Limited Co', 'Public Limited Co'), ('Partnership Co', 'Partnership Co'), ('Proprietorship', 'Proprietorship'), ('Gov Sector', 'Gov Sector'), ('Others', 'Others')], max_length=50)),
                ('gst_no', models.CharField(max_length=15)),
                ('pan_no', models.CharField(max_length=10)),
                ('company_status', models.CharField(choices=[('Manufacturer', 'Manufacturer'), ('Authorised Dealer', 'Authorised Dealer'), ('Stockist/Trader', 'Stockist/Trader'), ('Importer/Indian Agent', 'Importer/Indian Agent'), ('Service Provider', 'Service Provider')], max_length=50)),
                ('state', models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal')], max_length=50)),
                ('banking_name', models.CharField(max_length=255)),
                ('bank', models.CharField(max_length=255)),
                ('ifsc', models.CharField(max_length=11)),
                ('account_number', models.CharField(max_length=20)),
                ('address', models.TextField(default='Default Address')),
                ('std_code_phone_no', models.CharField(default='Default STD Code and Phone No.', max_length=20)),
                ('contact_person', models.CharField(default='Default Contact Person', max_length=255)),
                ('city', models.CharField(default='Default City', max_length=100)),
                ('fax', models.CharField(blank=True, default='Default Fax', max_length=20, null=True)),
                ('contact_person_designation', models.CharField(default='Default Designation', max_length=255)),
                ('website', models.URLField(blank=True, default='https://example.com', null=True)),
                ('is_msmse', models.BooleanField(default=False)),
                ('country', models.CharField(default='Default Country', max_length=50)),
                ('state_contact', models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal')], default='Andhra Pradesh', max_length=50)),
                ('mobile', models.CharField(default='0000000000', max_length=15)),
                ('business_description', models.TextField(default='Default Business Description')),
                ('email', models.EmailField(default='default@example.com', max_length=254)),
                ('pin', models.CharField(default='000000', max_length=10)),
            ],
        ),
    ]
