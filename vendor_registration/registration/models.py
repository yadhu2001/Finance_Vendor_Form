from django.db import models

class Vendor(models.Model):
    FIRM_TYPE_CHOICES = [
        ('Public Ltd Co', 'Public Ltd Co'),
        ('Private Ltd Co', 'Private Ltd Co'),
        ('LLP', 'LLP'),
        ('Partnership firm', 'Partnership firm'),
        ('Proprietorship', 'Proprietorship'),
        ('Others', 'Others'),
    ]

    COMPANY_STATUS_CHOICES = [
        ('Manufacturer', 'Manufacturer'),
        ('Authorised Dealer', 'Authorised Dealer'),
        ('Stockist/Trader', 'Stockist/Trader'),
        ('Importer/Indian Agent', 'Importer/Indian Agent'),
        ('Service Provider', 'Service Provider'),
    ]

    LAKSHYA_DEPARTMENT_CHOICES = [
        ('Admin Department', 'Admin Department'),
        ('IT Department', 'IT Department'),
        ('Marketing Department', 'Marketing Department'),
        ('Academic Department', 'Academic Department'),
        ('Finance/Legal Department', 'Finance/Legal Department'),
        ('HR Department', 'HR Department'),
    ]

    # ✅ New Field
    requesting_lakshya_department = models.CharField(
        max_length=50,
        choices=LAKSHYA_DEPARTMENT_CHOICES,
        verbose_name="Requesting Lakshya Department",
        null=True,
        blank=True
    )


    STATE_CHOICES = [
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal'),
    ]

    # Company Details
    vendor_name = models.CharField(max_length=255)
    vendor_type = models.CharField(max_length=50, choices=FIRM_TYPE_CHOICES)
    gst_no = models.CharField(max_length=15)
    pan_no = models.CharField(max_length=10)
    company_status = models.CharField(max_length=50, choices=COMPANY_STATUS_CHOICES)
    state = models.CharField(max_length=50, choices=STATE_CHOICES)
    banking_name = models.CharField(max_length=255)
    bank = models.CharField(max_length=255)
    ifsc = models.CharField(max_length=11)
    account_number = models.CharField(max_length=20)
    registration_certificate = models.FileField(upload_to='registration_certificates/', blank=True, null=True)
    bank_details = models.FileField(upload_to='bank_details/', blank=True, null=True)

    # Vendor Contact Information
    address = models.TextField()
    std_code_phone_no = models.CharField(max_length=20)
    contact_person = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    contact_person_designation = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)
    is_msmse = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')], default='No')
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    business_description = models.TextField()
    pin = models.CharField(max_length=10)

    # Attachment Section (existing)
    registration_certificate = models.FileField(upload_to='registration_certificates/', blank=True, null=True)
    bank_details = models.FileField(upload_to='bank_details/', blank=True, null=True)

    # ✅ New Attachment Fields
    pan_document = models.FileField(upload_to='pan_documents/', blank=True, null=True)
    msme_certificate = models.FileField(upload_to='msme_certificates/', blank=True, null=True)

    def __str__(self):
        return self.vendor_name

